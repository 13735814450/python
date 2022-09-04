# -*- coding:utf-8 -*-
import subprocess
import shutil
import argparse
import os
import sys
import time

__author__ = "zhaojianxing.vendor"
__email__ = "zhaojianxing.vendor@sensetime.com"
__version__ = "v1.0.0"


def agent(**kwargs):
    """
    cc_agent to generate code coverage result
    zip results and send it over http to cc_server
    receive results and return

    :input: next_commit_id, last_commit_id if comparing between two version
    :return: full result, diff result
    """
    cc_result = {"Message": None, "Data": None, "Status Code": "500", "Report_URL": None}

    coco_path = kwargs.get("coco_path")
    base_branch = kwargs.get("base_branch")
    current_branch = kwargs.get("current_branch")
    product = kwargs.get("product")
    version = kwargs.get("version")
    pipeline = kwargs.get("pipeline")
    repo_url = kwargs.get("repo_url")
    language = kwargs.get("language")
    coco = kwargs.get("coco")
    test_id = kwargs.get("test_id")

    # zip the jacoco results
    try:
        shutil.make_archive("jacoco_result", "zip", coco_path)
    except Exception as exception:
        cc_result["Message"] = "Cannot zip jacoco result directory: check if the jacoco result exists!"      
        return cc_result

    # get repo_name
    repo_name = repo_url.split("/")[-1].replace(".git", "")

    # 线上
    url = "http://10.198.65.119:6601/coverage/branch"
    # url = "http://0.0.0.0:6601/coverage/branch"
    payload = {'git_url': repo_url, 'base_branch': base_branch, 'current_branch': current_branch,
               'product_name': product, 'version': version,
               'pipeline_id': pipeline, 'repo_name': repo_name,
               'language': language, 'coco_tool': coco,
               'test_id': test_id}
    files = [
        ('coverage', ('jacoco_result.zip', open('jacoco_result.zip', 'rb'),
                      'application/zip'))]
    headers = {}

    try:
        import requests
    except ImportError:
        if sys.version > "3":
            pip_cmd = ["pip3 install requests"]
        else:
            pip_cmd = ["pip install requests"]
        # print(pip_cmd)
        ret_b = subprocess.Popen(pip_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_b, stderr_b = ret_b.communicate()
        # 给一个安装耗时
        time.sleep(10)

        if stderr_b.decode('utf-8') != "":
            cc_result["message"] = "{package}install package failed, Please check if the network is affected".format(package=pip_cmd)

        if "Successfully" in stdout_b:
            import requests

    try:
        # connect to cc_server
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        # check if connection to cc_server correct
    except requests.exceptions.ConnectionError:
        cc_result["Message"] = "Connection error: failed to connect to cc_server"
    else:
        # run correctly
        cc_result = response.text

    # remove the zip file
    os.remove("jacoco_result.zip")

    return cc_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter the repo info")
    parser.add_argument('--coco_path', type=str, required=True, help='The path to jacoco result directory')
    parser.add_argument('--current_branch', type=str, required=True, help='current branch of execution')
    parser.add_argument('--base_branch', type=str, required=True, help='the branch that needs to be compared;'
                                                                       ' this branch is the baseline')
    parser.add_argument('--repo_url', type=str, required=True, help='gitlab project http url')                                                            
    parser.add_argument('--product', type=str, default='Demo', help='The product name')
    parser.add_argument('--version', type=str, default='1.0.0', help='The version number of your product')
    parser.add_argument('--pipeline', type=str, default='no_input', help='The pipeline ID')
    parser.add_argument('--language', type=str, default='java', help='A list of code language included in repo;'
                                                                     ' separate by "," ')
    parser.add_argument('--coco', type=str, default='jacoco', help='A list of code coverage tool used in repo;'
                                                                   ' separate by ","')
    parser.add_argument('--test_id', type=str, required=True, help="test_id")
    args = parser.parse_args()
    args = vars(args)
    print(agent(**args))
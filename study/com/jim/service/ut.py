import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def mail(str):
    per=50
    data2=json.loads(str)
    val=data2['data']['diff']['diff_coverage']
    val=val*100
    # print(val)
    if val < per:
        print("no")
        body=json.dumps(data2,indent=2)
        mail_host="smtp.163.com"  #设置服务器
        mail_user="niming2001@163.com"    #用户名
        mail_pass="PIFPRWEAYGQOSCMK"   #口令
        sender = 'niming2001@163.com'
        receivers = ["wuxiaohong@sensetime.com","niming2001@163.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(body, 'plain', 'utf-8')
        # message['From'] = Header("sense link ut", 'utf-8')
        message['To'] = Header("ut alarm", 'utf-8')
        subject = 'the coverage percent of %d%% is below %d%% ' % (val,per)
        # print(subject)
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException as err:
            print ("Error: 无法发送邮件",err)
    else:
        print("ok")
    return


str='{"msg": "N/A", "data": {"full": {"covered_line": 0, "total_line": 60307, "line_coverage": 0.0}, "diff": {"covered_diff_line": 3, "total_diff_line": 17, "diff_coverage": 0.18}, "info": {"base_branch": "v2.6.4-20210824-apiv6", "base_commit_id": "aa8ac31f3a55468b936805ddd5d619ad8a33baa6", "current_branch": "v2.6.4-20210824-apiv6-wxh", "current_commit_id": "8b5260d8a1e82a2c017e2c9b7a3903ba0966e1aa"}}, "status_code": "200", "Report URL": "http://10.198.65.119:8999/cctool/sl-link/20220129020658/report"}'
mail(str)

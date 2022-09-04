import time
import datetime
from com.jim.service.study2 import *
from com.jim.service.People import *

def t1():
    s2="ddd"
    i=10
    val=s2+str(i)
    print(val)
    j=0
    while j<10:
        print(j)
        j+=1
    else:
        print(100)
    for k in range(10,20,2):
        print(k)
    return val

def lt():
    list=[1,2,3,5,6,7,8]
    print(list)
    list.append(11)
    print(list)
    print(list[3:5])
    list[4]=100
    print(list)
    del list[5]
    print(list)
    list.remove(3)
    print(list)
    print(max(list))
    print(min(list))
    print(len(list))
    list.sort()
    print(list)
    list.sort(reverse=True)
    print(list)

def lt2():
    list=("a","b","h","k","g","o")
    print(list)
    print(list[3:5])
    print(max(list))
    print(min(list))
    print(len(list))
    del list

def lt3():
    tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print(tinydict)
    print ("tinydict['Name']: ", tinydict['Name'])
    tinydict['Name']="wxh"
    print(tinydict)
    del tinydict['Name']
    print(tinydict)
    tinydict['address']="hangzhou"
    print(tinydict)
def lt4():
    st={'black','white','yellow','blue'}
    st1={'black','uuu','yellow','blue'}
    print(st)
    st.add('green')
    print(st)
    st.remove('black')
    print(st)
    st.update("hi")
    print(st)
    st.add('hhh')
    print(st)
    print(st1)
    st3 = st & st1
    print(st3)
    st3 = st | st1
    print(st3)
    st3 = st - st1
    print(st3)

def fl():
    file=open("d:\\tmp\\input.log","r",encoding='utf-8')
    file1=open("d:\\tmp\\out.log","w")
    line=file.readline()
    while line != "":
        print(line)
        file1.write(line)
        line=file.readline()
    else:
        print("finished")
    file.close()
    file1.close()
    return "OK"

def exp():
    try:
        apple=int(input('apple num: '))
        child=int(input('children num: '))
        num = apple/child
    except ZeroDivisionError as err:
        print(err.args)
    except ValueError as err:
        print(err.args)
    else:
        print("ok", num)
    finally:
        print("game over")

def cls():
    p=People("wxh",175,75)
    p.speak()
    print(p.weight)
def str():
    val = input("come on:")
    i1 = input("come on i:")
    print("begin " + val)
    print(i1)
    if val=="ok" and i1=="1":
      print(val)
    s1="hello word"
    i = 11
    print(s1)
    print(i)
    print("end")
    t1()
    t2()
def dt():
    t=time.time()
    d=datetime.datetime
    print(t)
    print(d)
    localtime = time.asctime( time.localtime(time.time()) )
    print ("本地时间为 :", localtime)
dt()


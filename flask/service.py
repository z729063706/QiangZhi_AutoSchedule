import app
import json
import requests
import pymysql
from getlesson import makesql
import pandas as pd
logger = app.logHelper.getToolLogger()
def savesheet(username, password,notice):
    session = requests.session()
    #jsessionid = redis_object.get(cookies_key)
    url = 'http://jwcnew.nefu.edu.cn/dblydx_jsxsd/'
    login_url = 'http://jwcnew.nefu.edu.cn/dblydx_jsxsd/xk/LoginToXk'
    logindata = {'USERNAME':username, 'PASSWORD':password}
    session.post(login_url,data=logindata)
    #re = session.get('http://jwcnew.nefu.edu.cn/dblydx_jsxsd/xskb/xskb_list.do?Ves632DSdyV=NEW_XSD_PYGL')
    f = session.get('http://jwcnew.nefu.edu.cn/dblydx_jsxsd/xskb/xskb_print.do?xnxq01id=2021-2022-2&zc=')
    try:
        f.content.decode('gbk')
        return '密码错误,请不要频繁提交！'
    except:
        mysql_conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'zzzyyyhhh', db= 'lesson')
        sql = "SELECT * FROM `profile` where id='{0}'".format(username)
        if mysql_conn.cursor().execute(sql) > 0:
            return '数据已存在,请勿重复提交,如需修改请联系管理员！'
        open('/Users/zhaoyunhao/Code/webapp/xls/{0}.xls'.format(username),'wb').write(f.content)
        return makesql(username,password,notice)


def getstudents(department):
    mysql_conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'zzzyyyhhh', db= 'lesson')
    if department == '':
        sql = "SELECT name,id,has_work,first_department,second_department FROM `profile`"
    else:
        sql = "SELECT name,id,has_work,first_department,second_department FROM `profile` WHERE second_department = '{0}'".format(department)
    se = mysql_conn.cursor()
    n = se.execute(sql)
    re = []    
    for i in range(n):
        re.append(se.fetchone())
    col = ['name','id','has_work','first_department','second_department']
    data = list(map(list, re))
    res = {}
    res['total'] = len(data)
    for i in range(len(data)):
        tmp = {}
        for j in range (len(data[i])):
            tmp[col[j]] = data[i][j]
        res[i] = tmp
    return res


def getfree(week,day,lesson):
    sql = 'select name,id from `profile` where substring(free{0}_{1},{2},1)=1'.format(day,lesson,week)
    mysql_conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'zzzyyyhhh', db= 'lesson')
    se = mysql_conn.cursor()
    n = se.execute(sql)
    re = []    
    for i in range(n):
        re.append(se.fetchone())
    return re
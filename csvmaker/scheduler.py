import pymysql
import csv
def getfreeweek(s):
    i = 0
    st = 0
    ed = 0
    r = []
    while i < 18:
        if s[i] == '1':
            st = i
            ed = i
            while s[i+1] == '1':
                ed = ed + 1
                if i < 17:
                    i = i + 1
                else:
                    break
            if st == ed:
                r.append(str(st+1))
            else:
                r.append("{0}—{1}".format(str(st+1),str(ed+1)))
        i = i + 1 
    res = ''
    for x in r:
        res = res + x + '、'
    return res[:-1]

def makenewline(r):
    notice = r[48]
    with open('/Users/zhaoyunhao/Code/webapp/xls/free.csv','a+',encoding='gbk') as f:
        writer = csv.writer(f)
        newline = [r[0],r[48]]
        for i in range(6,48):
            newline.append(getfreeweek(str(r[i])[2:-1]))
        writer.writerow(newline)
    return
        
mysql_conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'zzzyyyhhh', db= 'lesson')
sql = 'SELECT * FROM `profile` WHERE free1_1'
se = mysql_conn.cursor()
n = se.execute(sql)
re = []    
headline = ['姓名','备注','周一12','周一34','周一56','周一78','周一90','周一晚','周二12','周二34','周二56','周二78','周二90','周二晚','周三12','周三34','周三56','周三78','周三90','周三晚','周四12','周四34','周四56','周四78','周四90','周四晚','周五12','周五34','周五56','周五78','周五90','周五晚','周六12','周六34','周六56','周六78','周六90','周六晚','周日12','周日34','周日56','周日78','周日90','周日晚']
with open('/Users/zhaoyunhao/Code/webapp/xls/free.csv','w+',encoding='gbk') as f:
        writer = csv.writer(f)
        writer.writerow(headline)
for i in range(n):
    re.append(se.fetchone())
for r in re:
    makenewline(r)
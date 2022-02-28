import xlrd
import pymysql
def dec(ii,jj,table,totalweeks):
    lessons = table.row_values(ii, start_colx=0, end_colx=None)[jj].split('\n\n')
    MAX_WEEK_NUMBER = 23
    bz = [0]*MAX_WEEK_NUMBER 
    if lessons[0] == ' ':
        return bz,'1111111111111111111111'
    for lesson in lessons:
        if lesson == '':
            continue
        detail = lesson.split('\n')
        weekline = 2
        if detail[0] == '':
            weekline = weekline + 1
        weeks = detail[weekline][:-3].split(',')
        for week in weeks:
            if '-' in week:
                weekfromto = week.split('-')
                if '[' in weekfromto[1]:
                    weekfromto[1] = weekfromto[1][:-1]
                try:
                    for i in range(int(weekfromto[0]),int(weekfromto[1])+1):
                        bz[i] = 1
                        #print ('week {0},day {1},lesson {2} is busy!'.format(i,jj,ii-2))
                        totalweeks [i][jj][ii-2] = 1
                except:
                    print ("no")
            else:
                if '[' in week:
                    week = week[:-1]
                bz[int(week)] = 1
                #print ('week {0},day {1},lesson {2} is busy!'.format(week,jj,ii-2))
                totalweeks [int(week)][jj][ii-2] = 1
        #total = 0
        total = ''
        for i in range (1,23):
            #total = total + 2**i* bz[i]
            if bz[i] == 0:
                total = total + '1'
            else:
                total = total + '0'
    return bz,total

def makesql(id,password,notice):
    mysql_conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'zzzyyyhhh', db= 'lesson')
    stuid = id
    totalweeks = [[[0 for i in range(8)] for j in range (8)] for k in range (24)]
    data = xlrd.open_workbook('/Users/zhaoyunhao/Code/webapp/xls/{0}.xls'.format(id))
    table = data.sheets()[0]
    lesson = []
    alllesson = []
    students = '''
    test1
    test2
    '''.split('\n')
    stuname = table.row_values(0, start_colx=0, end_colx=None)[0].split(' ')[1]
    if stuname not in students:
        sql = "INSERT INTO profile(name,id,password) VALUES ('{0}',{1},'{2}')".format(stuname,stuid,password)
        try:
            with mysql_conn.cursor() as cursor:
                cursor.execute(sql)
            mysql_conn.commit()
        except Exception as e:
            mysql_conn.rollback()
            mysql_conn.close
        return "非本部成员，请联系管理员核实！"
    for i in range(3,9):
        day = []
        freeday = []
        for j in range(1,8):
            #print(i,j)
            bz = dec(i,j,table,totalweeks)[0]
            total = dec(i,j,table,totalweeks)[1]
            day.append(bz)
            freeday.append(total)
        lesson.append(day)
        alllesson.append(freeday)
    sql = "INSERT INTO profile(name,id,password,free1_1,free1_2,free1_3,free1_4,free1_5,free1_6,free2_1,free2_2,free2_3,free2_4,free2_5,free2_6,free3_1,free3_2,free3_3,free3_4,free3_5,free3_6,free4_1,free4_2,free4_3,free4_4,free4_5,free4_6,free5_1,free5_2,free5_3,free5_4,free5_5,free5_6,free6_1,free6_2,free6_3,free6_4,free6_5,free6_6,free7_1,free7_2,free7_3,free7_4,free7_5,free7_6,notice) VALUES ('{0}',{1},'{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}','{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}','{41}','{42}','{43}','{44}','{45}')".format(stuname,stuid,password,alllesson[0][0],alllesson[1][0],alllesson[2][0],alllesson[3][0],alllesson[4][0],alllesson[5][0],alllesson[0][1],alllesson[1][1],alllesson[2][1],alllesson[3][1],alllesson[4][1],alllesson[5][1],alllesson[0][2],alllesson[1][2],alllesson[2][2],alllesson[3][2],alllesson[4][2],alllesson[5][2],alllesson[0][3],alllesson[1][3],alllesson[2][3],alllesson[3][3],alllesson[4][3],alllesson[5][3],alllesson[0][4],alllesson[1][4],alllesson[2][4],alllesson[3][4],alllesson[4][4],alllesson[5][4],alllesson[0][5],alllesson[1][5],alllesson[2][5],alllesson[3][5],alllesson[4][5],alllesson[5][5],alllesson[0][6],alllesson[1][6],alllesson[2][6],alllesson[3][6],alllesson[4][6],alllesson[5][6],notice)
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
        mysql_conn.commit()
    except Exception as e:
        mysql_conn.rollback()
        mysql_conn.close
        return "服务异常，请联系管理员！"+str(e)        
    for i in range (1,23):
        sql1 = "INSERT INTO week{51}(name, stuid, d1_1, d1_2, d1_3, d1_4, d1_5, d1_6, d1_7, d2_1, d2_2, d2_3, d2_4, d2_5, d2_6, d2_7, d3_1, d3_2, d3_3, d3_4, d3_5, d3_6, d3_7, d4_1, d4_2, d4_3, d4_4, d4_5, d4_6, d4_7, d5_1, d5_2, d5_3, d5_4, d5_5, d5_6, d5_7, d6_1, d6_2, d6_3, d6_4, d6_5, d6_6, d6_7, d7_1, d7_2, d7_3, d7_4, d7_5, d7_6, d7_7) VALUES ('{0}','{1}', {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},{41},{42},{43},{44},{45},{46},{47},{48},{49},{50})" \
        .format(stuname,stuid,totalweeks[i][1][1],totalweeks[i][1][2],totalweeks[i][1][3],totalweeks[i][1][4],totalweeks[i][1][5],totalweeks[i][1][6],totalweeks[i][1][7],totalweeks[i][2][1],totalweeks[i][2][2],totalweeks[i][2][3],totalweeks[i][2][4],totalweeks[i][2][5],totalweeks[i][2][6],totalweeks[i][2][7],totalweeks[i][3][1],totalweeks[i][3][2],totalweeks[i][3][3],totalweeks[i][3][4],totalweeks[i][3][5],totalweeks[i][3][6],totalweeks[i][3][7],totalweeks[i][4][1],totalweeks[i][4][2],totalweeks[i][4][3],totalweeks[i][4][4],totalweeks[i][4][5],totalweeks[i][4][6],totalweeks[i][4][7],totalweeks[i][5][1],totalweeks[i][5][2],totalweeks[i][5][3],totalweeks[i][5][4],totalweeks[i][5][5],totalweeks[i][5][6],totalweeks[i][5][7],totalweeks[i][6][1],totalweeks[i][6][2],totalweeks[i][6][3],totalweeks[i][6][4],totalweeks[i][6][5],totalweeks[i][6][6],totalweeks[i][6][7],totalweeks[i][7][1],totalweeks[i][7][2],totalweeks[i][7][3],totalweeks[i][7][4],totalweeks[i][7][5],totalweeks[i][7][6],totalweeks[i][7][7],i)
        sql2 = "INSERT INTO lessons(name, stuid, week, d1_1, d1_2, d1_3, d1_4, d1_5, d1_6, d1_7, d2_1, d2_2, d2_3, d2_4, d2_5, d2_6, d2_7, d3_1, d3_2, d3_3, d3_4, d3_5, d3_6, d3_7, d4_1, d4_2, d4_3, d4_4, d4_5, d4_6, d4_7, d5_1, d5_2, d5_3, d5_4, d5_5, d5_6, d5_7, d6_1, d6_2, d6_3, d6_4, d6_5, d6_6, d6_7, d7_1, d7_2, d7_3, d7_4, d7_5, d7_6, d7_7) VALUES ('{0}','{1}', {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},{51})" \
        .format(stuname,stuid,i,totalweeks[i][1][1],totalweeks[i][1][2],totalweeks[i][1][3],totalweeks[i][1][4],totalweeks[i][1][5],totalweeks[i][1][6],totalweeks[i][1][7],totalweeks[i][2][1],totalweeks[i][2][2],totalweeks[i][2][3],totalweeks[i][2][4],totalweeks[i][2][5],totalweeks[i][2][6],totalweeks[i][2][7],totalweeks[i][3][1],totalweeks[i][3][2],totalweeks[i][3][3],totalweeks[i][3][4],totalweeks[i][3][5],totalweeks[i][3][6],totalweeks[i][3][7],totalweeks[i][4][1],totalweeks[i][4][2],totalweeks[i][4][3],totalweeks[i][4][4],totalweeks[i][4][5],totalweeks[i][4][6],totalweeks[i][4][7],totalweeks[i][5][1],totalweeks[i][5][2],totalweeks[i][5][3],totalweeks[i][5][4],totalweeks[i][5][5],totalweeks[i][5][6],totalweeks[i][5][7],totalweeks[i][6][1],totalweeks[i][6][2],totalweeks[i][6][3],totalweeks[i][6][4],totalweeks[i][6][5],totalweeks[i][6][6],totalweeks[i][6][7],totalweeks[i][7][1],totalweeks[i][7][2],totalweeks[i][7][3],totalweeks[i][7][4],totalweeks[i][7][5],totalweeks[i][7][6],totalweeks[i][7][7])
        try:
            with mysql_conn.cursor() as cursor:
                cursor.execute(sql1)
                cursor.execute(sql2)
            mysql_conn.commit()
        except Exception as e:
            mysql_conn.rollback()
            mysql_conn.close
            return "服务异常，请联系管理员！"+str(e)
    mysql_conn.close 

    return stuname+'的课表成功同步至服务器！'


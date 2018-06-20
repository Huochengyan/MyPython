#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "apphelper", "TESTDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from UserInfo")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

resultList=cursor.fetchall()
for row in resultList:
    print(row[0])
    print(row[1])
    print(row[2])

#print("Database version : %s " % data)

# 关闭数据库连接
db.close()




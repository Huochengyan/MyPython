import  pymysql
class DBHelper:

    def Exsql(self,sql):
        sql=sql.encode('utf-8')
        conn = pymysql.connect("localhost", "root", "apphelper", "TESTDB")
        # 打开数据库连接
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = conn .cursor()
        # 提交，不然无法保存新建或者修改的数据
        #sql=sql.decode('utf-8')
        result=cursor.execute(sql)
        conn.commit()
        # 关闭数据库连接
        cursor.close();
        conn.close();
        return result

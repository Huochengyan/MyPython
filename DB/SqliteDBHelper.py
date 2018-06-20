import sqlite3

class SqliteDBHelper:
    def ExSql(self, sql):
        #sql = sql.encode('utf-8')
        conn = sqlite3.connect('mySqlite.db')
        print("Opened database successfully");
        c = conn.cursor();
        result=c.execute(sql)
        conn.commit()
        conn.close()
        return result;
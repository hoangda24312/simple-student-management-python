import mysql.connector
class Database:
    def __init__(self):
        self.conn =mysql.connector.connect(
            host ="your host",
            password = "yourpass",
            user ="your name",
            database = "your database",
            use_pure = True
        )
        self.cursor = self.conn.cursor()
        print("Đã kết nối database thành công")
    
    def chay_lenh(self, query, params = None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
    
    def select(self, query, params = None):
        if params:
            self.cursor.execute(query,params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()



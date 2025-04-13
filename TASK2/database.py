import pymysql

class Database:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="quanly_banthietbi"
            )
            self.cursor = self.conn.cursor()
        except pymysql.MySQLError as e:
            print(f"Lỗi kết nối MySQL: {e}")
            raise

    def ket_noi(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            if query.strip().lower().startswith("select"):
                return self.cursor.fetchall()
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Lỗi truy vấn SQL: {e}")
            return None

    def bat_dau_giao_dich(self):
        self.conn.begin()

    def ket_thuc_giao_dich(self):
        self.conn.commit()

    def hoan_tac(self):
        self.conn.rollback()

    def dong_ket_noi(self):
        self.cursor.close()
        self.conn.close()
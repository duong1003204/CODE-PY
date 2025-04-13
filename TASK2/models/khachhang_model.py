from TASK2.database import Database

class KhachHangModel:
    def __init__(self):
        self.db = Database()

    def them_khachhang(self, ten, sdt, email, diachi):
        query = "INSERT INTO khachhang (ten, sdt, email, diachi) VALUES (%s, %s, %s, %s)"
        return self.db.ket_noi(query, (ten, sdt, email, diachi))

    def sua_khachhang(self, id, ten, sdt, email, diachi):
        query = "UPDATE khachhang SET ten=%s, sdt=%s, email=%s, diachi=%s WHERE id=%s"
        return self.db.ket_noi(query, (ten, sdt, email, diachi, id))

    def xoa_khachhang(self, id):
        query = "DELETE FROM khachhang WHERE id=%s"
        return self.db.ket_noi(query, (id,))

    def tim_khachhang(self, keyword):
        query = "SELECT * FROM khachhang WHERE ten LIKE %s OR sdt LIKE %s"
        return self.db.ket_noi(query, (f"%{keyword}%", f"%{keyword}%"))

    def lay_tat_ca_khachhang(self):
        query = "SELECT * FROM khachhang"
        return self.db.ket_noi(query)

    def dong_ket_noi(self):
        self.db.dong_ket_noi()
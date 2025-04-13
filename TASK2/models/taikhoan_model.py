from TASK2.database import   Database

class TaiKhoanModel:
    def __init__(self):
        self.db = Database()

    def kiem_tra_dang_nhap(self, ten_dang_nhap, mat_khau):
        query = "SELECT * FROM taikhoan WHERE ten_dang_nhap=%s AND mat_khau=%s"
        result = self.db.ket_noi(query, (ten_dang_nhap, mat_khau))
        return result[0] if result else None

    def dong_ket_noi(self):
        self.db.dong_ket_noi()
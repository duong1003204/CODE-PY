from TASK2.database import Database




class ThongKeModel:
    def __init__(self):
        self.db = Database()

    def thong_ke_hoadon(self, tu_ngay, den_ngay):
        query = """
        SELECT h.id, h.ngaylap, h.tongtien, k.ten AS ten_khachhang 
        FROM hoadon h 
        LEFT JOIN khachhang k ON h.id_khachhang = k.id 
        WHERE h.ngaylap BETWEEN %s AND %s
        """
        return self.db.ket_noi(query, (tu_ngay, den_ngay))

    def dong_ket_noi(self):
        self.db.dong_ket_noi()
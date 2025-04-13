from TASK2.database import Database

class HoaDonModel:
    def __init__(self):
        self.db = Database()

    def them_hoadon(self, id_khachhang, ngay_lap, tongtien):
        query = "INSERT INTO hoadon (id_khachhang, ngaylap, tongtien) VALUES (%s, %s, %s)"
        self.db.ket_noi(query, (id_khachhang, ngay_lap, tongtien))
        query_id = "SELECT LAST_INSERT_ID() AS id"
        result = self.db.ket_noi(query_id)
        return result[0][0] if result else None

    def them_chitiethoadon(self, id_hoadon, id_thietbi, soluong, dongia):
        query = "INSERT INTO chitiethoadon (id_hoadon, id_thietbi, soluong, dongia) VALUES (%s, %s, %s, %s)"
        return self.db.ket_noi(query, (id_hoadon, id_thietbi, soluong, dongia))

    def lay_hoadon_theo_ngay(self, tu_ngay, den_ngay):
        query = """
        SELECT h.id, h.ngaylap, h.tongtien, k.ten AS ten_khachhang 
        FROM hoadon h 
        LEFT JOIN khachhang k ON h.id_khachhang = k.id
        WHERE h.ngaylap BETWEEN %s AND %s
        """
        return self.db.ket_noi(query, (tu_ngay, den_ngay))

    def dong_ket_noi(self):
        self.db.dong_ket_noi()
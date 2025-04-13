from TASK2.database import Database

class NhanVienModel:
    def __init__(self):
        self.db = Database()

    def lay_tat_ca_nhanvien(self):
        query = "SELECT id, HoTen, VaiTro, TenDangNhap FROM nhanvien"
        return self.db.ket_noi(query)

    def them_nhanvien(self, hoten, vaitro, tendangnhap, matkhau):
        query = "INSERT INTO nhanvien (HoTen, VaiTro, TenDangNhap, MatKhau) VALUES (%s, %s, %s, %s)"
        return self.db.ket_noi(query, (hoten, vaitro, tendangnhap, matkhau))

    def sua_nhanvien(self, id_nhanvien, hoten, vaitro, tendangnhap, matkhau):
        query = """
        UPDATE nhanvien 
        SET HoTen = %s, VaiTro = %s, TenDangNhap = %s, MatKhau = %s 
        WHERE id = %s
        """
        values = (hoten, vaitro, tendangnhap, matkhau if matkhau else None, id_nhanvien)
        return self.db.ket_noi(query, values)

    def xoa_nhanvien(self, id_nhanvien):
        query = "DELETE FROM nhanvien WHERE id = %s"
        return self.db.ket_noi(query, (id_nhanvien,))

    def tim_kiem_nhanvien(self, tu_khoa):
        query = """
        SELECT id, HoTen, VaiTro, TenDangNhap 
        FROM nhanvien 
        WHERE HoTen LIKE %s OR TenDangNhap LIKE %s
        """
        tu_khoa = f"%{tu_khoa}%"
        return self.db.ket_noi(query, (tu_khoa, tu_khoa))

    def kiem_tra_tendangnhap(self, tendangnhap, id_nhanvien=None):
        query = "SELECT id FROM nhanvien WHERE TenDangNhap = %s"
        values = (tendangnhap,)
        if id_nhanvien:
            query += " AND id != %s"
            values = (tendangnhap, id_nhanvien)
        result = self.db.ket_noi(query, values)
        return bool(result)

    def dong_ket_noi(self):
        self.db.dong_ket_noi()
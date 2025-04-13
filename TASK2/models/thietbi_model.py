from TASK2.database import  Database


class ThietBiModel:
    def __init__(self):
        self.db = Database()

    def them_thietbi(self, ten, hang, gia, soluong, mota, hinhanh):
        query = "INSERT INTO thietbi (ten, hang, gia, soluong, mota, hinhanh) VALUES (%s, %s, %s, %s, %s, %s)"
        return self.db.ket_noi(query, (ten, hang, gia, soluong, mota, hinhanh))

    def sua_thietbi(self, id, ten, hang, gia, soluong, mota, hinhanh):
        query = "UPDATE thietbi SET ten=%s, hang=%s, gia=%s, soluong=%s, mota=%s, hinhanh=%s WHERE id=%s"
        return self.db.ket_noi(query, (ten, hang, gia, soluong, mota, hinhanh, id))

    def xoa_thietbi(self, id):
        query = "DELETE FROM thietbi WHERE id=%s"
        return self.db.ket_noi(query, (id,))

    def tim_thietbi(self, keyword):
        query = "SELECT * FROM thietbi WHERE ten LIKE %s"
        return self.db.ket_noi(query, (f"%{keyword}%",))

    def lay_tat_ca_thietbi(self):
        query = "SELECT * FROM thietbi"
        return self.db.ket_noi(query)


    def lay_thietbi_theo_id(self, id_thietbi):
        query = "SELECT soluong FROM thietbi WHERE id = %s"
        result = self.db.ket_noi(query, (id_thietbi,))
        return result[0][0] if result else 0

    def cap_nhat_soluong(self, id_thietbi, soluong):
        query = "UPDATE thietbi SET soluong = soluong - %s WHERE id = %s"
        return self.db.ket_noi(query, (soluong, id_thietbi))

    def dong_ket_noi(self):
        self.db.dong_ket_noi()
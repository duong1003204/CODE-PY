import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt6.uic import loadUi
from PyQt6.QtCore import QDate
from TASK2.database import Database
from TASK2.models.hoadon_model import HoaDonModel
from TASK2.models.khachhang_model import KhachHangModel
from TASK2.models.thietbi_model import ThietBiModel

class HoaDonForm(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "..", "ui", "HoaDonForm.ui")
        loadUi(ui_path, self)
        self.tongtien = 0
        self.danh_sach_thietbi = []

        self.dateNgayLap.setDate(QDate.currentDate())
        self.dateTuNgay.setDate(QDate.currentDate().addDays(-30))
        self.dateDenNgay.setDate(QDate.currentDate())

        self.btnThemSP.clicked.connect(self.them_sanpham)
        self.btnXoaSP.clicked.connect(self.xoa_sanpham)
        self.btnLuuHD.clicked.connect(self.luu_hoadon)
        self.btnXemHD.clicked.connect(self.xem_hoadon)
        self.btnThoat.clicked.connect(self.thoat)
        self.txtTimKiemSP.textChanged.connect(self.tim_kiem_sanpham)

        self.load_khachhang()
        self.load_sanpham()

    def load_khachhang(self):
        model = KhachHangModel()
        khachhang_list = model.lay_tat_ca_khachhang()
        self.comboKhachHang.clear()
        for khachhang in khachhang_list:
            self.comboKhachHang.addItem(khachhang[1], khachhang[0])  # Tên và ID
        model.dong_ket_noi()

    def load_sanpham(self):
        model = ThietBiModel()
        sanpham_list = model.lay_tat_ca_thietbi()
        self.tableSanPham.setColumnCount(7)
        self.tableSanPham.setHorizontalHeaderLabels(["ID", "Tên", "Nhà sản xuất", "Giá", "Số lượng", "Mô tả", "ảnh"])
        self.tableSanPham.setRowCount(0)
        if sanpham_list:
            self.tableSanPham.setRowCount(len(sanpham_list))
            for row_index, row_data in enumerate(sanpham_list):
                for col_index, value in enumerate(row_data):
                    self.tableSanPham.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        model.dong_ket_noi()

    def tim_kiem_sanpham(self):
        tu_khoa = self.txtTimKiemSP.text().lower()
        model = ThietBiModel()
        sanpham_list = model.lay_tat_ca_thietbi()
        filtered_list = [sp for sp in sanpham_list if tu_khoa in str(sp[1]).lower() or tu_khoa in str(sp[0])]
        self.tableSanPham.setRowCount(0)
        self.tableSanPham.setColumnCount(7)
        self.tableSanPham.setHorizontalHeaderLabels(["ID", "Tên", "Nhà sản xuất", "Giá", "Số lượng", "Mô tả", "ảnh"])
        if filtered_list:
            self.tableSanPham.setRowCount(len(filtered_list))
            for row_index, row_data in enumerate(filtered_list):
                for col_index, value in enumerate(row_data):
                    self.tableSanPham.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        model.dong_ket_noi()

    def them_sanpham(self):
        selected_row = self.tableSanPham.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn một sản phẩm để thêm!")
            return

        id_thietbi = self.tableSanPham.item(selected_row, 0).text()
        ten = self.tableSanPham.item(selected_row, 1).text()
        gia = float(self.tableSanPham.item(selected_row, 3).text())
        ton_kho = int(self.tableSanPham.item(selected_row, 4).text())

        for sp in self.danh_sach_thietbi:
            if sp['id_thietbi'] == id_thietbi:
                QMessageBox.warning(self, "Thông báo", "Sản phẩm đã có trong giỏ hàng, vui lòng chỉnh sửa số lượng!")
                return

        soluong, ok = QInputDialog.getInt(self, "Nhập số lượng", "Số lượng:", 1, 1, ton_kho)
        if ok:
            if soluong > ton_kho:
                QMessageBox.warning(self, "Thông báo", f"Chỉ còn {ton_kho} sản phẩm trong kho!")
                return
            thanh_tien = gia * soluong
            self.tongtien += thanh_tien

            # Cập nhật bảng chi tiết hóa đơn
            row_count = self.tableChiTietHD.rowCount()
            self.tableChiTietHD.setColumnCount(4)
            self.tableChiTietHD.setHorizontalHeaderLabels(["ID Thiết bị", "Tên", "Số lượng", "Thành tiền"])
            self.tableChiTietHD.setRowCount(row_count + 1)
            self.tableChiTietHD.setItem(row_count, 0, QTableWidgetItem(str(id_thietbi)))
            self.tableChiTietHD.setItem(row_count, 1, QTableWidgetItem(ten))
            self.tableChiTietHD.setItem(row_count, 2, QTableWidgetItem(str(soluong)))
            self.tableChiTietHD.setItem(row_count, 3, QTableWidgetItem(str(thanh_tien)))

            self.danh_sach_thietbi.append({'id_thietbi': id_thietbi, 'soluong': soluong, 'dongia': gia})
            self.lblTongTien.setText(f"Tổng tiền: {self.tongtien}")

    def xoa_sanpham(self):
        selected_row = self.tableChiTietHD.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn sản phẩm để xóa!")
            return

        reply = QMessageBox.question(self, "Xác nhận", "Bạn có chắc muốn xóa sản phẩm này?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            thanh_tien = float(self.tableChiTietHD.item(selected_row, 3).text())
            id_thietbi = self.tableChiTietHD.item(selected_row, 0).text()

            self.tongtien -= thanh_tien
            self.danh_sach_thietbi = [sp for sp in self.danh_sach_thietbi if sp['id_thietbi'] != id_thietbi]
            self.tableChiTietHD.removeRow(selected_row)
            self.lblTongTien.setText(f"Tổng tiền: {self.tongtien}")

    def luu_hoadon(self):
        if not self.danh_sach_thietbi:
            QMessageBox.warning(self, "Thông báo", "Vui lòng thêm sản phẩm vào hóa đơn!")
            return

        id_khachhang = self.comboKhachHang.currentData()
        ngay_lap = self.dateNgayLap.date().toString("yyyy-MM-dd")
        if not id_khachhang:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn khách hàng!")
            return

        model = HoaDonModel()
        thietbi_model = ThietBiModel()
        model.db.bat_dau_giao_dich()
        try:
            id_hoadon = model.them_hoadon(id_khachhang, ngay_lap, self.tongtien)
            if id_hoadon:
                for thietbi in self.danh_sach_thietbi:
                    model.them_chitiethoadon(id_hoadon, thietbi['id_thietbi'], thietbi['soluong'], thietbi['dongia'])
                    thietbi_model.cap_nhat_soluong(thietbi['id_thietbi'], thietbi['soluong'])
                model.db.ket_thuc_giao_dich()
                QMessageBox.information(self, "Thành công", "Lưu hóa đơn thành công!")
                self.tableChiTietHD.setRowCount(0)
                self.tongtien = 0
                self.danh_sach_thietbi = []
                self.lblTongTien.setText("Tổng tiền: 0")
                self.load_sanpham()
            else:
                raise Exception("Không thể tạo hóa đơn")
        except Exception as e:
            model.db.hoan_tac()
            QMessageBox.critical(self, "Lỗi", f"Lưu hóa đơn thất bại: {e}")
        model.dong_ket_noi()
        thietbi_model.dong_ket_noi()

    def xem_hoadon(self):
        tu_ngay = self.dateTuNgay.date().toString("yyyy-MM-dd")
        den_ngay = self.dateDenNgay.date().toString("yyyy-MM-dd")
        model = HoaDonModel()
        hoadon_list = model.lay_hoadon_theo_ngay(tu_ngay, den_ngay)
        self.tableChiTietHD.setColumnCount(4)
        self.tableChiTietHD.setHorizontalHeaderLabels(["ID", "Ngày lập", "Tổng tiền", "Khách hàng"])
        self.tableChiTietHD.setRowCount(0)
        if hoadon_list:
            self.tableChiTietHD.setRowCount(len(hoadon_list))
            for row_index, row_data in enumerate(hoadon_list):
                for col_index, value in enumerate(row_data):
                    self.tableChiTietHD.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        model.dong_ket_noi()

    def thoat(self):
        if self.danh_sach_thietbi:
            reply = QMessageBox.question(
                self, "Xác nhận", "Bạn có chắc muốn thoát? Dữ liệu chưa lưu sẽ mất!",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply != QMessageBox.StandardButton.Yes:
                return
        if self.role == "Admin":
            from TASK2.forms.main_window import TrangChu
            self.main_window = TrangChu(role="Admin")  # Truyền role rõ ràng
        else:
            from TASK2.forms.main_windowNV import TrangChu1
            self.main_window = TrangChu1(role=self.role if self.role else "NhanVien")  # Dự phòng
        self.main_window.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = HoaDonForm()
#     window.show()
#     sys.exit(app.exec())
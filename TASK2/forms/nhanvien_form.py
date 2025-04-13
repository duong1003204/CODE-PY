import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from TASK2.database import Database
from TASK2.models.nhanvien_model import NhanVienModel

class NhanVienForm(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "..", "ui", "NhanVienForm.ui")
        loadUi(ui_path, self)
        self.selected_id = None

        self.btnThem.clicked.connect(self.them_nhanvien)
        self.btnSua.clicked.connect(self.sua_nhanvien)
        self.btnXoa.clicked.connect(self.xoa_nhanvien)
        self.btnTim.clicked.connect(self.tim_kiem_nhanvien)
        self.btnThoat.clicked.connect(self.thoat)
        self.tableNhanVien.itemSelectionChanged.connect(self.chon_nhanvien)

        self.load_nhanvien()

    def load_nhanvien(self):
        model = NhanVienModel()
        nhanvien_list = model.lay_tat_ca_nhanvien()
        self.tableNhanVien.setColumnCount(4)
        self.tableNhanVien.setHorizontalHeaderLabels(["ID", "Họ tên", "Vai trò", "Tên đăng nhập"])
        self.tableNhanVien.setRowCount(0)
        if nhanvien_list:
            self.tableNhanVien.setRowCount(len(nhanvien_list))
            for row_index, row_data in enumerate(nhanvien_list):
                for col_index, value in enumerate(row_data):
                    self.tableNhanVien.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        model.dong_ket_noi()

    def them_nhanvien(self):
        hoten = self.txtHoTen.text().strip()
        vaitro = self.comboVaiTro.currentText()
        tendangnhap = self.txtTenDangNhap.text().strip()
        matkhau = self.txtMatKhau.text().strip()

        if not hoten or not tendangnhap or not matkhau:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đầy đủ họ tên, tên đăng nhập và mật khẩu!")
            return

        model = NhanVienModel()
        if model.kiem_tra_tendangnhap(tendangnhap):
            QMessageBox.warning(self, "Thông báo", "Tên đăng nhập đã tồn tại!")
            model.dong_ket_noi()
            return

        if model.them_nhanvien(hoten, vaitro, tendangnhap, matkhau):
            QMessageBox.information(self, "Thành công", "Thêm nhân viên thành công!")
            self.load_nhanvien()
            self.xoa_truong_nhap()
        else:
            QMessageBox.critical(self, "Lỗi", "Thêm nhân viên thất bại!")
        model.dong_ket_noi()

    def sua_nhanvien(self):
        if not self.selected_id:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn nhân viên để sửa!")
            return

        hoten = self.txtHoTen.text().strip()
        vaitro = self.comboVaiTro.currentText()
        tendangnhap = self.txtTenDangNhap.text().strip()
        matkhau = self.txtMatKhau.text().strip()

        if not hoten or not tendangnhap:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đầy đủ họ tên và tên đăng nhập!")
            return

        model = NhanVienModel()
        if model.kiem_tra_tendangnhap(tendangnhap, self.selected_id):
            QMessageBox.warning(self, "Thông báo", "Tên đăng nhập đã tồn tại!")
            model.dong_ket_noi()
            return

        if model.sua_nhanvien(self.selected_id, hoten, vaitro, tendangnhap, matkhau):
            QMessageBox.information(self, "Thành công", "Sửa nhân viên thành công!")
            self.load_nhanvien()
            self.xoa_truong_nhap()
            self.selected_id = None
        else:
            QMessageBox.critical(self, "Lỗi", "Sửa nhân viên thất bại!")
        model.dong_ket_noi()

    def xoa_nhanvien(self):
        if not self.selected_id:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn nhân viên để xóa!")
            return

        reply = QMessageBox.question(self, "Xác nhận", "Bạn có chắc muốn xóa nhân viên này?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            model = NhanVienModel()
            if model.xoa_nhanvien(self.selected_id):
                QMessageBox.information(self, "Thành công", "Xóa nhân viên thành công!")
                self.load_nhanvien()
                self.xoa_truong_nhap()
                self.selected_id = None
            else:
                QMessageBox.critical(self, "Lỗi", "Xóa nhân viên thất bại!")
            model.dong_ket_noi()

    def tim_kiem_nhanvien(self):
        tu_khoa = self.txtTimKiem.text().strip().lower()
        model = NhanVienModel()
        nhanvien_list = model.tim_kiem_nhanvien(tu_khoa)
        self.tableNhanVien.setRowCount(0)
        self.tableNhanVien.setColumnCount(4)
        self.tableNhanVien.setHorizontalHeaderLabels(["ID", "Họ tên", "Vai trò", "Tên đăng nhập"])
        if nhanvien_list:
            self.tableNhanVien.setRowCount(len(nhanvien_list))
            for row_index, row_data in enumerate(nhanvien_list):
                for col_index, value in enumerate(row_data):
                    self.tableNhanVien.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        model.dong_ket_noi()

    def chon_nhanvien(self):
        selected_row = self.tableNhanVien.currentRow()
        if selected_row != -1:
            self.selected_id = int(self.tableNhanVien.item(selected_row, 0).text())
            self.txtHoTen.setText(self.tableNhanVien.item(selected_row, 1).text())
            self.comboVaiTro.setCurrentText(self.tableNhanVien.item(selected_row, 2).text())
            self.txtTenDangNhap.setText(self.tableNhanVien.item(selected_row, 3).text())
            self.txtMatKhau.clear()
        else:
            self.selected_id = None
            self.xoa_truong_nhap()

    def xoa_truong_nhap(self):
        self.txtHoTen.clear()
        self.comboVaiTro.setCurrentIndex(0)
        self.txtTenDangNhap.clear()
        self.txtMatKhau.clear()

    def thoat(self):
        from TASK2.forms.main_window import TrangChu
        self.main_window = TrangChu(role="Admin")  # Luôn là Admin vì chỉ Admin vào được
        self.main_window.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = NhanVienForm()
#     window.show()
#     sys.exit(app.exec())
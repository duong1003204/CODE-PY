import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from TASK2.database import Database
from TASK2.models.khachhang_model import KhachHangModel

class KhachHangForm(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "..", "ui", "KhachHangForm.ui")
        loadUi(ui_path, self)
        if self.role == "NhanVien":
            self.btnSuaKH.setEnabled(False)
            self.btnXoaKH.setEnabled(False)
        # ... phần còn lại của __init__ giữ nguyên ...

        self.btnThemKH.clicked.connect(self.them)
        self.btnSuaKH.clicked.connect(self.sua)
        self.btnXoaKH.clicked.connect(self.xoa)
        self.btnTimKH.clicked.connect(self.tim_kiem)
        self.btnThoat.clicked.connect(self.thoat)
        self.tableKhachHang.cellClicked.connect(self.hien_thi_thong_tin)
        self.load_data()

    def thoat(self):
        if self.role == "Admin":
            from TASK2.forms.main_window import TrangChu
            self.main_window = TrangChu(role="Admin")  # Truyền role rõ ràng
        else:
            from TASK2.forms.main_windowNV import TrangChu1
            self.main_window = TrangChu1(role=self.role if self.role else "NhanVien")  # Dự phòng
        self.main_window.show()
        self.close()

    def lam_moi(self):
        self.txtTenKH.clear()
        self.txtSDT.clear()
        self.txtEmail.clear()
        self.txtDiaChi.clear()

    def hien_thi_thong_tin(self, row):
        self.txtTenKH.setText(self.tableKhachHang.item(row, 1).text())
        self.txtSDT.setText(self.tableKhachHang.item(row, 2).text())
        self.txtEmail.setText(self.tableKhachHang.item(row, 3).text())
        self.txtDiaChi.setText(self.tableKhachHang.item(row, 4).text())

    def load_data(self):
        model = KhachHangModel()
        rows = model.lay_tat_ca_khachhang()
        if rows:
            self.tableKhachHang.setRowCount(len(rows))
            self.tableKhachHang.setColumnCount(5)
            for row_index, row_data in enumerate(rows):
                for col_index, value in enumerate(row_data):
                    self.tableKhachHang.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        else:
            print("❌ Không có dữ liệu hoặc lỗi khi truy vấn.")
        model.dong_ket_noi()

    def them(self):
        ten = self.txtTenKH.text().strip()
        sdt = self.txtSDT.text().strip()
        email = self.txtEmail.text().strip()
        diachi = self.txtDiaChi.text().strip()

        if not all([ten, sdt, email, diachi]):
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đủ thông tin!")
            return

        model = KhachHangModel()
        result = model.them_khachhang(ten, sdt, email, diachi)
        if result:
            QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công!")
            self.load_data()
            self.lam_moi()
        else:
            QMessageBox.critical(self, "Lỗi", "Thêm khách hàng thất bại!")
        model.dong_ket_noi()

    def sua(self):
        if self.role != "Admin":
            return
        selected_row = self.tableKhachHang.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn một khách hàng để sửa!")
            return

        id = self.tableKhachHang.item(selected_row, 0).text()
        ten = self.txtTenKH.text().strip()
        sdt = self.txtSDT.text().strip()
        email = self.txtEmail.text().strip()
        diachi = self.txtDiaChi.text().strip()

        if not all([ten, sdt, email, diachi]):
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đủ thông tin!")
            return

        model = KhachHangModel()
        result = model.sua_khachhang(id, ten, sdt, email, diachi)
        if result:
            QMessageBox.information(self, "Thành công", "Sửa khách hàng thành công!")
            self.load_data()
            self.lam_moi()
        else:
            QMessageBox.critical(self, "Lỗi", "Sửa khách hàng thất bại!")
        model.dong_ket_noi()

    def xoa(self):
        if self.role != "Admin":
            return
        selected_row = self.tableKhachHang.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn một khách hàng để xóa!")
            return

        id = self.tableKhachHang.item(selected_row, 0).text()

        if QMessageBox.question(
                self,
                "Xác nhận",
                f"Bạn có chắc muốn xóa khách hàng có mã {id} không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
        ) != QMessageBox.StandardButton.Yes:
            return

        model = KhachHangModel()
        result = model.xoa_khachhang(id)
        if result:
            QMessageBox.information(self, "Thành công", "Xóa khách hàng thành công!")
            self.load_data()
            self.lam_moi()
        else:
            QMessageBox.critical(self, "Lỗi", "Xóa khách hàng thất bại!")
        model.dong_ket_noi()

    def tim_kiem(self):
        keyword = self.txtTimKH.text().strip()
        model = KhachHangModel()
        rows = model.tim_khachhang(keyword)
        if rows:
            self.tableKhachHang.setRowCount(len(rows))
            self.tableKhachHang.setColumnCount(5)
            for row_index, row_data in enumerate(rows):
                for col_index, value in enumerate(row_data):
                    self.tableKhachHang.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        else:
            self.tableKhachHang.setRowCount(0)
        model.dong_ket_noi()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = KhachHangForm()
#     window.show()
#     sys.exit(app.exec())
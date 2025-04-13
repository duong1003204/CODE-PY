import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
from TASK2.database import Database
from TASK2.models.thietbi_model import ThietBiModel

class ThietBiForm(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "..", "ui", "ThietBiForm.ui")
        loadUi(ui_path, self)
        self.hinhanh_path = ""
        if self.role == "NhanVien":
            self.btnSua.setEnabled(False)
            self.btnXoa.setEnabled(False)

        self.btnChonAnh.clicked.connect(self.chon_anh)
        self.btnThem.clicked.connect(self.them)
        self.btnSua.clicked.connect(self.sua)
        self.btnXoa.clicked.connect(self.xoa)
        self.btnTim.clicked.connect(self.tim_kiem)
        self.btnThoat.clicked.connect(self.thoat)
        self.tableThietBi.cellClicked.connect(self.hien_thi_thong_tin)
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
        self.txtTen.clear()
        self.txtHang.clear()
        self.txtGia.clear()
        self.txtSoLuong.clear()
        self.txtMoTa.clear()
        self.lblHinhAnh.clear()
        self.hinhanh_path = ""

    def chon_anh(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.hinhanh_path = file_name
            pixmap = QPixmap(file_name)
            self.lblHinhAnh.setPixmap(pixmap.scaled(300, 300))

    def hien_thi_thong_tin(self, row):
        self.txtTen.setText(self.tableThietBi.item(row, 1).text())
        self.txtHang.setText(self.tableThietBi.item(row, 2).text())
        self.txtGia.setText(self.tableThietBi.item(row, 3).text())
        self.txtSoLuong.setText(self.tableThietBi.item(row, 4).text())
        self.txtMoTa.setText(self.tableThietBi.item(row, 5).text())
        hinh_anh = self.tableThietBi.item(row, 6).text()
        if hinh_anh:
            self.hinhanh_path = hinh_anh
            pixmap = QPixmap(hinh_anh)
            self.lblHinhAnh.setPixmap(pixmap.scaled(300, 300))

    def load_data(self):
        model = ThietBiModel()
        rows = model.lay_tat_ca_thietbi()
        if rows:
            self.tableThietBi.setRowCount(len(rows))
            self.tableThietBi.setColumnCount(7)
            for row_index, row_data in enumerate(rows):
                for col_index, value in enumerate(row_data):
                    self.tableThietBi.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        else:
            print("❌ Không có dữ liệu hoặc lỗi khi truy vấn.")
        model.dong_ket_noi()

    def them(self):
        ten = self.txtTen.text().strip()
        hang = self.txtHang.text().strip()
        gia = self.txtGia.text().strip()
        soluong = self.txtSoLuong.text().strip()
        mota = self.txtMoTa.text().strip()
        hinhanh = self.hinhanh_path

        if not all([ten, hang, gia, soluong, mota]):
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đủ thông tin!")
            return

        try:
            gia = float(gia)
            soluong = int(soluong)
        except ValueError:
            QMessageBox.warning(self, "Thông báo", "Giá và số lượng phải là số!")
            return

        model = ThietBiModel()
        result = model.them_thietbi(ten, hang, gia, soluong, mota, hinhanh)
        if result:
            QMessageBox.information(self, "Thành công", "Thêm thiết bị thành công!")
            self.load_data()
            self.lam_moi()
        else:
            QMessageBox.critical(self, "Lỗi", "Thêm thiết bị thất bại!")
        model.dong_ket_noi()

    def sua(self):
        if self.role != "Admin":
            return  # Đã vô hiệu hóa nút, nhưng thêm kiểm tra cho chắc
        selected_row = self.tableThietBi.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn một thiết bị để sửa!")
            return

        id = self.tableThietBi.item(selected_row, 0).text()
        ten = self.txtTen.text().strip()
        hang = self.txtHang.text().strip()
        gia = self.txtGia.text().strip()
        soluong = self.txtSoLuong.text().strip()
        mota = self.txtMoTa.text().strip()
        hinhanh = self.hinhanh_path

        if not all([ten, hang, gia, soluong, mota]):
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đủ thông tin!")
            return

        try:
            gia = float(gia)
            soluong = int(soluong)
        except ValueError:
            QMessageBox.warning(self, "Thông báo", "Giá và số lượng phải là số!")
            return

        model = ThietBiModel()
        result = model.sua_thietbi(id, ten, hang, gia, soluong, mota, hinhanh)
        if result:
            QMessageBox.information(self, "Thành công", "Sửa thiết bị thành công!")
            self.load_data()
            self.lam_moi()
        else:
            QMessageBox.critical(self, "Lỗi", "Sửa thiết bị thất bại!")
        model.dong_ket_noi()

    def xoa(self):
        if self.role != "Admin":
            return
        selected_row = self.tableThietBi.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn một thiết bị để xóa!")
            return

        id = self.tableThietBi.item(selected_row, 0).text()

        if QMessageBox.question(
                self,
                "Xác nhận",
                f"Bạn có chắc muốn xóa thiết bị có mã {id} không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
        ) != QMessageBox.StandardButton.Yes:
            return

        model = ThietBiModel()
        result = model.xoa_thietbi(id)
        if result:
            QMessageBox.information(self, "Thành công", "Xóa thiết bị thành công!")
            self.load_data()
            self.lam_moi()
        else:
            QMessageBox.critical(self, "Lỗi", "Xóa thiết bị thất bại!")
        model.dong_ket_noi()

    def tim_kiem(self):
        keyword = self.txtTimKiem.text().strip()
        model = ThietBiModel()
        rows = model.tim_thietbi(keyword)
        if rows:
            self.tableThietBi.setRowCount(len(rows))
            self.tableThietBi.setColumnCount(7)
            for row_index, row_data in enumerate(rows):
                for col_index, value in enumerate(row_data):
                    self.tableThietBi.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        else:
            self.tableThietBi.setRowCount(0)
        model.dong_ket_noi()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ThietBiForm()
#     window.show()
#     sys.exit(app.exec())
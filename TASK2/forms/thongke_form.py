import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from TASK2.database import Database
from TASK2.models.thongke_model import ThongKeModel

class ThongKeForm(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "..", "ui", "ThongKeForm.ui")
        loadUi(ui_path, self)
        self.btnThongKe.clicked.connect(self.thong_ke)
        self.btnThoat.clicked.connect(self.thoat)
        self.model = QStandardItemModel()
        self.tableThongKe.setModel(self.model)

    def thoat(self):
        if self.role == "Admin":
            from TASK2.forms.main_window import TrangChu
            self.main_window = TrangChu(role="Admin")  # Truyền role rõ ràng
        else:
            from TASK2.forms.main_windowNV import TrangChu1
            self.main_window = TrangChu1(role=self.role if self.role else "NhanVien")  # Dự phòng
        self.main_window.show()
        self.close()

    def thong_ke(self):
        tu_ngay = self.dateTuNgay.date().toString("yyyy-MM-dd")
        den_ngay = self.dateDenNgay.date().toString("yyyy-MM-dd")
        model = ThongKeModel()
        thongke_list = model.thong_ke_hoadon(tu_ngay, den_ngay)

        self.model.clear()

        if thongke_list:
            self.model.setHorizontalHeaderLabels(["ID", "Ngày lập", "Tổng tiền", "Khách hàng"])
            for row_data in thongke_list:
                row_items = [QStandardItem(str(value)) for value in row_data]
                self.model.appendRow(row_items)
        else:
            QMessageBox.information(self, "Thông báo", "Không có hóa đơn nào trong khoảng thời gian này!")
            self.model.setHorizontalHeaderLabels(["ID", "Ngày lập", "Tổng tiền", "Khách hàng"])

        model.dong_ket_noi()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ThongKeForm()
#     window.show()
#     sys.exit(app.exec())
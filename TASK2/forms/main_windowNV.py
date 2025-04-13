import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from TASK2.forms.login_form import DangNhap

class TrangChu1(QMainWindow):
    def __init__(self, role=None):
        super().__init__()
        self.role = role
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "..", "ui", "MainWindowNV.ui")
        loadUi(ui_path, self)
        self.btnDangXuat.clicked.connect(self.dang_xuat)
        self.btnThietBi.clicked.connect(self.mo_form_thietbi)
        self.btnKhachHang.clicked.connect(self.mo_form_khachhang)
        self.btnHoaDon.clicked.connect(self.mo_form_hoadon)
        self.btnThongKe.clicked.connect(self.mo_form_thongke)

    def mo_form_thietbi(self):
        from TASK2.forms.thietbi_form import ThietBiForm
        self.thietbi_form = ThietBiForm(role=self.role)
        self.hide()
        self.thietbi_form.show()

    def mo_form_khachhang(self):
        from TASK2.forms.khachhang_form import KhachHangForm
        self.khachhang_form = KhachHangForm(role=self.role)
        self.hide()
        self.khachhang_form.show()

    def mo_form_hoadon(self):
        from TASK2.forms.hoadon_form import HoaDonForm
        self.hoadon_form = HoaDonForm(role=self.role)
        self.hide()
        self.hoadon_form.show()

    def mo_form_thongke(self):
        from TASK2.forms.thongke_form import ThongKeForm
        self.thongke_form = ThongKeForm(role=self.role)
        self.hide()
        self.thongke_form.show()

    def dang_xuat(self):
        self.dang_nhap = DangNhap()
        self.dang_nhap.show()
        self.close()
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = TrangChu1()
#     window.show()
#     sys.exit(app.exec())
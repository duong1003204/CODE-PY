import sys
from PyQt6.QtWidgets import QApplication
from TASK2.forms.login_form import DangNhap


def main():
    app = QApplication(sys.argv)

    login_window = DangNhap()
    login_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
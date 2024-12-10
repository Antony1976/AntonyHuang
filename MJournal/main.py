# file:main.py
import sys
from PySide6.QtWidgets import QApplication, QWidget
from UI.mj_main_window_ui import Ui_Form


class MJMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
     app = QApplication(sys.argv)

mj_window = MJMainWindow()
mj_window.show()
sys.exit(app.exec())

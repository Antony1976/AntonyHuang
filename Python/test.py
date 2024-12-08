import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QLabel

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)

"""Module providingFunction print test."""
print("Test Python Program ~")
print("What happen ?")
# input()

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.resize(800, 600)
label.show()
app.exec()
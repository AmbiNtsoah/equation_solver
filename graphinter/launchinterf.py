import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle ( "This is my first pyqt5 app!")
win.show()
win.setGeometry(100, 100 , 400 , 400)

sys.exit(app.exec_())
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QPixMap


#Subclass of QMainWindow
class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maestro")
        #Setting the size
        screen_size = QApplication.primaryScreen().geometry()
        windowWidth = screen_size.width() // 2
        windowHeight = screen_size.height() // 2 
        self.setGeometry(0, 0, windowWidth, windowHeight)
        

app = QApplication(sys.argv)
window = MainWindow()

#Setting background color to black
#palette = QPalette()
#palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.blue)
#window.setPalette(palette)
        
window.show()

app.exec()
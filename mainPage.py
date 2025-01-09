import random
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

app = QApplication(sys.argv)

screen_size = QApplication.primaryScreen().geometry()
windowWidth = screen_size.width()
windowHeight = screen_size.height()

#Subclass of QMainWindow
class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maestro")
        #Setting the size
        self.setGeometry(0, 0, windowWidth, windowHeight)
        self.setStyleSheet("""
        background: Black;                
        """)
        self.createUI()

    def createUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        #Window Icon
        self.setWindowIcon(QIcon("titleImage.png"))
        #Title Image
        label = QLabel(self)
        pixmap = QPixmap('titleImage.png')
        label.setPixmap(pixmap)
        label.setGeometry((windowWidth // 2 )- 275, 0, 500, 500)
        self.createInteraction()

    def createInteraction(self):
        layout = QVBoxLayout()
        #Load the segmentation model
        segButton = QPushButton(text="Segmentation Model", parent=self)
        segButton.clicked.connect(self.segModelLoading)
        segButton.setFixedSize(250, 100)
        segButton.setStyleSheet("""
        font-size: 24px;
        background-color: "gold";
        """)
        segButton.move(100, windowHeight - 800)
        layout.addWidget(segButton)

        #Load the bounding boxes
        bbButton = QPushButton(text="Object Detection Model", parent=self)
        bbButton.clicked.connect(self.bbModelLoading)
        bbButton.setFixedSize(250, 100)
        bbButton.setStyleSheet("""
        font-size: 23px;
        background-color: "gold";
        """)
        bbButton.move(100, windowHeight - 1000)
        layout.addWidget(segButton)
    
    def segModelLoading(self):
        print("Loading Segmentation Model")

    def bbModelLoading(self):
        print("Loading Object Detection Model")

    def customModel1(self):
        print("Loading Custom Model 1")

    def customModel2(self):
        print("Loading Custom Model 2")
        
window = MainWindow()
window.show()
app.exec()
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import subprocess
import signal
import os

app = QApplication(sys.argv)

screen_size = QApplication.primaryScreen().geometry()
windowWidth = screen_size.width()
windowHeight = screen_size.height()

# Worker class to run subprocess in a separate thread
class Worker(QThread):
    finished = pyqtSignal()  # Signal to indicate task completion
    error = pyqtSignal(str)  # Signal to indicate errors

    def __init__(self, command, parent=None):
        super().__init__(parent)
        self.command = command
        self.process = None  # Keep track of the subprocess

    def run(self):
        try:
            # Start the subprocess
            self.process = subprocess.Popen(self.command, preexec_fn=os.setsid)
            self.process.wait()  # Wait for the process to complete
            self.finished.emit()
        except Exception as e:
            self.error.emit(f"Error: {e}")

    def terminate(self):
        # Terminate the subprocess if it's running
        if self.process and self.process.poll() is None:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.finished.emit()

# Subclass of QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maestro")
        self.setGeometry(0, 0, windowWidth, windowHeight)
        self.setStyleSheet("background: Black;")
        self.worker = None  # Initialize the worker attribute

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid = QGridLayout()
        self.central_widget.setLayout(self.grid)

        self.createUI()

    def createUI(self):
        # Window Icon
        self.setWindowIcon(QIcon("titleImage.png"))
        # Title Image
        label = QLabel(self)
        pixmap = QPixmap('titleImage.png')
        label.setPixmap(pixmap)
        label.setGeometry((windowWidth // 2) - 300, 0, 500, 500)

        self.createInteraction()

    def createInteraction(self):
        # Load the segmentation model
        segButton = QPushButton("Segmentation Model", self)
        segButton.clicked.connect(self.segModelLoading)
        segButton.setFixedSize(250, 100)
        segButton.setStyleSheet("font-size: 24px; background-color: gold;")
        segButton.move(100, windowHeight - 800)

        # Load the bounding boxes
        bbButton = QPushButton("Object Detection Model", self)
        bbButton.clicked.connect(self.bbModelLoading)
        bbButton.setFixedSize(250, 100)
        bbButton.setStyleSheet("font-size: 23px; background-color: gold;")
        bbButton.move(100, windowHeight - 1000)

        #Custom Model 1
        c1Button = QPushButton("Custom Model 1", self)
        c1Button.clicked.connect(self.customModel1)
        c1Button.setFixedSize(250, 100)
        c1Button.setStyleSheet("font-size: 23px; background-color: gold;")
        c1Button.move(windowHeight + 250, windowHeight - 1000)

        #Custom Model 2
        c2Button = QPushButton("Custom Model 2", self)
        c2Button.clicked.connect(self.customModel1)
        c2Button.setFixedSize(250, 100)
        c2Button.setStyleSheet("font-size: 23px; background-color: gold;")
        c2Button.move(windowHeight + 250, windowHeight - 800)

    def segModelLoading(self):
        print("Loading Segmentation Model")
        self.runThread(["python", "segmentationModel.py"])

    def bbModelLoading(self):
        print("Loading Object Detection Model")
        self.runThread(["python", "boundingBoxModel.py"])
    
    def customModel1(self):
        print("Loading Your Custom Model - 1")
        self.runThread(["python", "customModel1.py"])

    def runThread(self, command):
        # Terminate any existing worker before starting a new one
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()

        # Start a new worker thread
        self.worker = Worker(command)
        self.worker.finished.connect(self.onTaskFinished)
        self.worker.error.connect(self.onTaskError)
        self.worker.start()

    def onTaskFinished(self):
        QMessageBox.information(self, "Success", "Task completed successfully!")

    def onTaskError(self, message):
        QMessageBox.critical(self, "Error", message)

window = MainWindow()
window.show()
app.exec()
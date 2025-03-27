import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QColor, QLinearGradient
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'HTML Web Scraper'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 700
        self.initUI()
  
    def initUI(self):
        # Set the window title
        self.setWindowTitle(self.title)
        
        # Define the geometry of the window
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Define the button
        button_1 = QPushButton('Hello', self)
        
        # Show a tooltip when hovering over the button
        button_1.setToolTip('This is an example button')
        
        # Move the button
        button_1.move(100, int(self.width - (self.width * 0.2)))
        
        # Connect the button clicks
        button_1.clicked.connect(self.button1_clicked)
        
        # Get the screen geometry
        screen_geometry = QApplication.primaryScreen().geometry()

        # Get the window geometry
        window_geometry = self.geometry()

        # Calculate the coordinates to center the window
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2

        # Move the window to the calculated position
        self.move(x, y)
        
        self.show()

    def button1_clicked(self):
        print("Button 1 clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
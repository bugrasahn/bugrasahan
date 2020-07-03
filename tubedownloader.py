import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pytube import YouTube

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.ustmenu()
        self.anamenu()
        self.show()

    def anamenu(self):
        widget = QWidget()
        h_box = QHBoxLayout()

        yazı = QLabel("lütfen link giriniz..")
        self.link = QLineEdit()
        self.link.setPlaceholderText("https://www.youtube.com/watch?v=ngbIQAeqpao")
        buton = QPushButton("indir")


        buton.clicked.connect(self.indir)
        buton.setShortcut("CTRL + D")

        h_box.addWidget(yazı)
        h_box.addWidget(self.link)
        h_box.addWidget(buton)


        widget.setLayout(h_box)
        self.setCentralWidget(widget)




    def ustmenu(self):
        self.setWindowTitle("Bugra Sahan -- Youtube Downloader")
        self.setWindowIcon(QIcon("youtube.png"))
        #boyut ayarları
        self.setGeometry(250,250,600,100)
        self.setMaximumSize(800,100)
        self.setMinimumSize(600,100)

    def indir(self):
        url = self.link.text()
        YouTube(url).streams.get_highest_resolution().download()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
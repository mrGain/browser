import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar starts here
        navbar = QToolBar()
        self.addToolBar(navbar)

        btn_back = QAction('Back',self)
        btn_back.triggered.connect(self.browser.back)
        navbar.addAction(btn_back)
        
        btn_forward = QAction('Forward',self)
        btn_forward.triggered.connect(self.browser.forward)
        navbar.addAction(btn_forward)
        
        btn_reload = QAction('Reload',self)
        btn_reload.triggered.connect(self.browser.reload)
        navbar.addAction(btn_reload)
        
        btn_home = QAction('Home',self)
        btn_home.triggered.connect(self.navigate_home)
        navbar.addAction(btn_home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://github.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Browser by Rakesh')
window = MainWindow()
app.exec_()                
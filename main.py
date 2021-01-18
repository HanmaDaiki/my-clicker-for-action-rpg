from template import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import pyautogui as p
import keyboard as k

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startBut.clicked.connect(self.clickStart)
        
    def clickStart(self):
        h1 = self.ui.lineHotKey.text()
        h2 = self.ui.lineHotKey_2.text()
        h3 = self.ui.lineHotKey_3.text()
        h4 = self.ui.lineHotKey_4.text()
        h5 = self.ui.lineHotKey_5.text()
        h6 = self.ui.lineHotKey_6.text()
        
        m = self.ui.lineMainKey.text()
        
        while True:
            try:  
                if k.is_pressed(m):
                    p.press(h1)            
                    p.press(h2)                    
                    p.press(h3)     
                    p.press(h4)           
                    p.press(h5)
                    p.press(h6)
                    continue
                elif k.is_pressed('f11'):
                    print('bye')
                    break
                else:
                    pass
            except:
                break 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
#见PyQt5中文教程 http://code.py40.com/pyqt5/16.html

import sys
#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication,QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("自媒体多平台发布系统")
        self.show()
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

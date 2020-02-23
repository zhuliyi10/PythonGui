#见PyQt5中文教程 http://code.py40.com/pyqt5/16.html

import sys
#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout,QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        vbox=QVBoxLayout()

        videoBox=QHBoxLayout()
        btnVideo = QPushButton('选择视频')
        btnVideo.clicked.connect(self.showVideoDialog)
        self.videoPath=QLabel()
        videoBox.addWidget(btnVideo)
        videoBox.addWidget(self.videoPath)
        videoBox.addStretch(1)
        vbox.addLayout(videoBox)

        picBox=QHBoxLayout()
        btnPic = QPushButton('设置封面')
        btnPic.clicked.connect(self.showPicDialog)
        self.picPath=QLabel()
        picBox.addWidget(btnPic)
        picBox.addWidget(self.picPath)
        picBox.addStretch(1)
        vbox.addLayout(picBox)

        titleBox=QHBoxLayout()
        titleBox.addWidget(QLabel("标题"))
        titleBox.addWidget(QLineEdit())
    
        vbox.addLayout(titleBox)

        descBox=QHBoxLayout()
        descBox.addWidget(QLabel("描述"))
        descBox.addWidget(QLineEdit())
     
        vbox.addLayout(descBox)

        btnRelease = QPushButton('发布')
        btnRelease.clicked.connect(self.release)
        vbox.addWidget(btnRelease)

        self.setLayout(vbox)
        # self.resize(600,400)
        self.setWindowTitle("自媒体多平台发布系统")
        self.show()

    def showVideoDialog(self):
        fname=QFileDialog.getOpenFileName(self,"选择文件")
        if fname[0]:
            self.videoPath.setText(fname[0])

    def showPicDialog(self):
        fname=QFileDialog.getOpenFileName(self,"选择文件")
        if fname[0]:
            self.picPath.setText(fname[0])

    def release(self):
        pass
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

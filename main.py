# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os, linecache, random


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(QtGui.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1188, 696)
        self.buttonStyle = "width: 30px;  height: 30px; color: #73ff38; text-align:center; padding: 5px;  margin: 5px;  border: 3px solid #73ff38;  float: left; border-radius: 15px;  text-align: justify;  font-size: 32px;"
        self.buttonStyleHitted = "width: 30px;  height: 30px; color: #FF0000; text-align:center; padding: 5px;  margin: 5px;  border: 3px solid #FF0000;  float: left; border-radius: 15px;  text-align: justify;  font-size: 32px;"
        MainWindow.setStyleSheet(_fromUtf8("background-color: black;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.buttons = []
        self.setUpKeyboard()
        self.mainwindow = MainWindow
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 150, 450, 280))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutWidget.setStyleSheet("background-image: url(img/s0.jpg);")
        self.keyWord = self.shuffleQuestion().rstrip()
        self.keyWord = self.keyWord.upper()
        self.keyWordHidden = ""
        self.setHiddenKeyword()
        self.updateHiddenWord()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.wrongChoiceCount = 0
        self.setUpCounter()

    def setHiddenKeyword(self):


        for i in range(len(self.keyWord)):
            if self.keyWord[i] == " ":
                self.keyWordHidden += " "
            elif self.keyWord[i] == "-":
                self.keyWordHidden += "-"
            else:
                self.keyWordHidden += "_"

    def shuffleQuestion(self):

        randomline = linecache.getline(os.getcwd()+"/words/words.txt", random.randrange(0, 356043))
        print(randomline)
        if randomline != "":
            return randomline
        else:
            return -1

    def setUpKeyboard(self):

        y = j = i = 0
        for i in range(26):
            if i%6==0 and i != 0:
                y+=1
                j = 0
                if y == 4:
                    j = 2
            self.buttons.insert(i,QtGui.QPushButton(self.centralwidget))
            self.buttons[i].setGeometry(QtCore.QRect(700 + 70*j, 166 + 70*y, 61, 61))
            self.buttons[i].setStyleSheet(_fromUtf8(self.buttonStyle))
            self.buttons[i].setObjectName(_fromUtf8("pushButton" + str(i)))
            self.buttons[i].setText(_translate("MainWindow", chr(ord('A') + i), None))
            self.buttons[i].setShortcut(str( chr(ord('A') + i)))
            self.buttons[i].clicked.connect(self.printme)
            self.buttons[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            j+=1

    def printme(self):

        result = ""
        sender = self.sender()
        for i in range(len(self.keyWord)):
            if self.keyWord[i] == sender.text():
                result = result + sender.text()     # Adds guess to string if guess is correctly
            else:
                # Add the dash at index i to result if it doesn't match the guess
                result = result + self.keyWordHidden[i]
                #use full ABSOLUTE path to the image, not relative

        if sender.text() not in self.keyWord:
            sender.clicked.disconnect()
            sender.setStyleSheet(self.buttonStyleHitted)
            self.updateCounter()
            if self.wrongChoiceCount == 9:
                self.clearViev()
                self.newScreen(0)
                return print("GAME OVER")

        self.keyWordHidden = result
        self.wordLabel.setText(self.keyWordHidden)
        self.wordLabel.show()
        print(self.keyWordHidden)
        self.updateHiddenWord()
        if self.keyWordHidden.upper() == self.keyWord:
            self.clearViev()
            self.newScreen(1)


    def clearViev(self):
        for i in range(26):
            self.buttons[i].setParent(None)
        self.counterLabel.setParent(None)
        self.keyWordHidden = ""
        self.formLayoutWidget.setParent(None)


    def newScreen(self, status):

        self.restartButton = QtGui.QPushButton(self.centralwidget)
        self.restartButton.setObjectName(_fromUtf8("restartButton"))
        self.restartButton.setGeometry(500, 250, 200, 50)
        self.restartButton.setText("Play Again")
        self.restartButton.setStyleSheet("background-color: #FFFFFF; color: #000000; width: 90px; height: 60px; font-size: 24px;")
        self.restartButton.show()
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.exitButton.setGeometry(750, 250, 200, 50)
        self.exitButton.setText("Exit")
        self.resultLabel = QtGui.QLabel(self.centralwidget)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.resultLabel.setGeometry(500, 50, 450, 100)
        self.resultLabel.show()
        self.exitButton.setStyleSheet("background-color: #FFFFFF; color: #000000; width: 90px; height: 60px; font-size: 24px;")
        self.exitButton.show()
        if status == 1:
            self.successScreen()
        elif status == 0:
            self.defeatScreen()
        self.exitButton.clicked.connect(sys.exit)
        self.restartButton.clicked.connect(self.restartGame)

    def successScreen(self):
        self.resultLabel.setText("SUCCESS!")
        self.resultLabel.setStyleSheet("color: #73FF38; font-size:90px;")

    def defeatScreen(self):
        self.resultLabel.setText("DEFEAT!")
        self.resultLabel.setStyleSheet("color: #FF0000; font-size:90px;")
        self.keyWordHidden = self.keyWord
        self.wordLabel.setParent(None)
        self.wordLabel = QtGui.QLabel(self.centralwidget)
        self.wordLabel.setObjectName(_fromUtf8("wordLabel"))
        self.wordLabel.setGeometry(1, 550, 1188, 100)
        self.wordLabel.setText(self.keyWordHidden)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setCapitalization(QtGui.QFont.AllUppercase)
        font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 12)
        self.wordLabel.setFont(font)
        self.wordLabel.setStyleSheet("color: #FFFFFF;")
        self.wordLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.wordLabel.show()
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 0, 400, 800))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutWidget.setStyleSheet("background-image: url(img/rope.png);")
        self.formLayoutWidget.show()

    def restartGame(self):
        self.wordLabel.setParent(None)
        self.resultLabel.setParent(None)
        self.setupUi(self.mainwindow)


    def updateHiddenWord(self):
        self.wordLabel = QtGui.QLabel(self.centralwidget)
        self.wordLabel.setObjectName(_fromUtf8("wordLabel"))
        self.wordLabel.setGeometry(1, 550, 1188, 100)
        self.wordLabel.setText(self.keyWordHidden)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setCapitalization(QtGui.QFont.AllUppercase)
        font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 12)
        self.wordLabel.setFont(font)
        self.wordLabel.setStyleSheet("color: #FFFFFF;")
        self.wordLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


    def setUpCounter(self):
        self.counterLabel = QtGui.QLabel(self.centralwidget)
        self.counterLabel.setObjectName(_fromUtf8("counterLabel"))
        self.counterLabel.setGeometry(1, 10, 150, 40)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.counterLabel.setFont(font)
        self.counterLabel.setStyleSheet("color: #FFFFFF")
        self.wrongChoiceCount = 0
        self.counterLabel.setText("Chances left: " + str(9 - self.wrongChoiceCount))

    def updateCounter(self):
        self.wrongChoiceCount+=1
        self.counterLabel.setText("Chances left: " + str(9 - self.wrongChoiceCount))
        self.formLayoutWidget.setStyleSheet("background-image: url(img/s" + str(self.wrongChoiceCount) + ".jpg);")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hangman", None))




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    print("SETUPED")
    mainWindow.show()
    input()
    # sys.exit(app.exec_())

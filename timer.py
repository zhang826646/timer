# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import datetime
import os
import subprocess


from PyQt5 import QtCore, QtGui, QtWidgets


def cmd(command):
    # celect=subprocess.Popen('SCHTASKS /QUERY /tn auto_shutdown', shell=True, encoding="utf-8")
    # celect_list=celect.stdout.readlines()
    # print(celect_list,'\n',celect_list[-1])
    # if celect_list and ('auto_shutdown' in celect_list[-1]):
    #     print('dsfsdfsd')
    #     b = subprocess.Popen(r'schtasks /delete /tn "auto_shutdown"', shell=True, encoding="utf-8",stdout=subprocess.PIPE)  # python执行cmd命令的方法
    #     b = subprocess.Popen(r'y', shell=True, encoding="utf-8",stdout=subprocess.PIPE)
    #     print(b.stdout.readlines(),'mmmmm')
    # print(celect.__dict__)
    subp=subprocess.Popen(command, shell=True, encoding="utf-8")
    # subp.communicate('y')
    print(subp.stdout.readlines(), 'mmmmm')
    subp.wait(2)
    print(subp.__dict__)
    if subp.poll() == 0:
        print(subp.communicate()[1])
    else:
        print("失败")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 241)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 10, 61, 51))
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("intValue", 19)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(200, 10, 61, 51))
        self.lcdNumber_3.setDigitCount(2)
        self.lcdNumber_3.setProperty("intValue", 19)
        self.lcdNumber_3.setObjectName("lcdNumber_3")

        # 创建定时器
        self.Timer = QtCore.QTimer()
        self.Timer.start(500)
        self.Timer.timeout.connect(self.TimeUpdate)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 16, 41))
        self.label.setStyleSheet("font: 72pt \"Adobe Arabic\";")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setIndent(-9)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 16, 41))
        self.label_2.setStyleSheet("font: 72pt \"Adobe Arabic\";")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setIndent(-9)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_2.setObjectName("label_2")
        # 定时时间
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 100, 20, 41))
        self.label_3.setStyleSheet("font: 72pt \"Adobe Arabic\";")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setIndent(-9)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_3.setObjectName("label_3")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(130, 100, 71, 51))
        self.spinBox_3.setStyleSheet("font: 100 26pt \"Adobe 黑体 Std R\";\n""")
        self.spinBox_3.setMaximum(59)
        self.spinBox_3.setProperty("value", "%02d" % 0)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(30, 100, 71, 51))
        self.spinBox_4.setStyleSheet("font: 100 26pt \"Adobe 黑体 Std R\";\n""")
        self.spinBox_4.setMaximum(24)
        self.spinBox_4.setProperty("value", "%02d" % 0)
        self.spinBox_4.setObjectName("spinBox_4")


        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(250, 100, 89, 16))
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 130, 89, 16))
        self.radioButton_2.setStyleSheet("font: 75 9pt \"Adobe Arabic\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(250, 170, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.AutoShutdown)
        self.buttonBox.rejected.connect(self.del_AutoShutdown)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 221, 20))
        self.label_4.setStyleSheet("font: 75 9pt \"Adobe 楷体 Std R\";")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "专属定时关机"))
        self.label.setText(_translate("MainWindow", ":"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.radioButton.setText(_translate("MainWindow", "仅此一次"))
        self.radioButton_2.setText(_translate("MainWindow", "每天"))
        self.label_4.setText(_translate("MainWindow", "你知道我在想你"))



    def TimeUpdate(self):
        today=datetime.datetime.today()
        self.lcdNumber.display("%02d" % today.hour)
        self.lcdNumber_2.display("%02d" % today.minute)
        self.lcdNumber_3.display("%02d" % today.second)

    def AutoShutdown(self):
        hour = self.spinBox_4.text().zfill(2)
        minute = self.spinBox_3.text().zfill(2)
        print(hour,minute)
        # os.system('chcp 65001')
        cmd_str=''
        if self.radioButton.isChecked() == True:
            cmd_str = f'schtasks /create /tn "auto_shutdown" /tr "shutdown /s /t 300" /sc once /st {hour}:{minute}:00 /f'
            print(f'{hour}:{minute}:00 进行一次自动关机')
        elif self.radioButton_2.isChecked() == True:
            cmd_str = f'schtasks /create /tn "auto_shutdown" /tr "shutdown /s /t 300" /sc daily /st {hour}:{minute}:00 /f'
            print(f'{hour}:{minute}:00 进行每天自动关机')
        else:
            self.label_4.setText('请勾选计划规则')
        if cmd_str:

            subp = subprocess.Popen(cmd_str, shell=False, encoding="utf-8")
            self.label_4.setText('已设置定时任务')

    def del_AutoShutdown(self):
        a = QtWidgets.QMessageBox.question(None, '提示', '删除定时任务点击”yes“ \n取消本次关机点击"no"', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)      #"退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        cond = False
        print(a)
        if a == QtWidgets.QMessageBox.Yes:
            cond = True
        # os.system('chcp 65001')
        try:
            subprocess.Popen(r'shutdown -a', shell=False,encoding="utf-8")  # python执行cmd命令的方法
            if cond:
                a=subprocess.Popen(r'schtasks /delete /tn "auto_shutdown" /f',shell=True, encoding="utf-8")  # python执行cmd命令的方法
                print(a.__dict__)
        except:
            pass
        self.label_4.setText('取消定时任务')





if __name__=="__main__":
    import sys
    os.system('chcp 65001')
    app=QtWidgets.QApplication(sys.argv)
    Mainwindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
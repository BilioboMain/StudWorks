
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import matplotlib.pyplot as plt
import math
import numpy as np
import pylab
import os
import pylab
import scipy.integrate as integrate
import scipy.special as special



def Lagr(x, y, n, t):
    z = 0
    for j in range(0, n):
        p1 = 1
        p2 = 1
        for i in range(0, n):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + (y[j] * p1) / p2
    return z

A=[0,0,0,0]
t=[0,0,0,0]
def gauss(X,Y,s):
    if s ==1:
        t[0]=0
        A[0]=2
    elif s==2:
        t[0] = -0.5773503 # -1 / sqrt(3)
        t[1] = 0.5773503 #1 / sqrt(3)
        A[0] = 1
        A[1] = 1
    elif s==3:
        t[0] = -0.7745967 #-sqrt(3 / 5);
        t[1] = 0
        t[2] = 0.7745967# sqrt(3 / 5);
        A[0] = 0.5555556 # 5 / 9;
        A[1] = 0.8888889 # 8 / 9;
        A[2] = 0.5555556 # 5 / 9;
    elif s==4:
        t[0] = -0.8611363# -sqrt((15 + 2 * sqrt(30)) / 35);
        t[1] = -0.3399810#-sqrt((15 - 2 * sqrt(30)) / 35);
        t[2] = 0.3399810#sqrt((15 - 2 * sqrt(30)) / 35);
        t[3] = 0.8611363# sqrt((15 + 2 * sqrt(30)) / 35);
        A[0] = 0.3478548# (18 - sqrt(30)) / 36;
        A[2] = 0.6521451# (18 + sqrt(30)) / 36;
        A[3] = 0.3478548# (18 - sqrt(30)) / 36;
    I =0

    for i in range(1,len(X)):
        a=X[i-1]
        b=X[i]
        I_k=0
        for j in range(s):
            x=0.5*(b+a+(b-a)*t[j])
            I_k = I_k+A[j]*Lagr(X,Y,len(X),x)
        I = I+(b-a)/2*I_k
    return I

class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'Третья работа'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button_draw= QPushButton('построить график и вывести значения в файл', self)
        button_draw.setToolTip('This is an example button')
        button_draw.move(150, 240)
        button_draw.clicked.connect(self.make_graf)

        button_interpol = QPushButton('Интерполировать', self)
        button_interpol.setToolTip('This is an example button')
        button_interpol.move(150, 270)
        button_interpol.clicked.connect(self.interpolirovat)

        button_integral = QPushButton('Интегрировать', self)
        button_integral.setToolTip('This is an example button')
        button_integral.move(150, 400)
        button_integral.clicked.connect(self.integrirovat)




        self.a = QLineEdit(self)
        self.a.move(150,60)
        self.a.resize(280,40)

        self.b = QLineEdit(self)
        self.b.move(150, 120)
        self.b.resize(280, 40)

        self.n = QLineEdit(self)
        self.n.move(150, 190)
        self.n.resize(280, 40)

        self.knutNumber = QLineEdit(self)
        self.knutNumber.move(150, 350)
        self.knutNumber.resize(280, 40)

        button_draw = QPushButton('a', self)
        button_draw.setToolTip('This is a')
        button_draw.move(150,30)

        button_draw = QPushButton('b', self)
        button_draw.setToolTip('This is b')
        button_draw.move(150, 95)

        button_draw = QPushButton('n', self)
        button_draw.setToolTip('This is n')
        button_draw.move(150, 160)

        self.show()
    @pyqtSlot()
    def make_graf(self):
        print('drawing')
        #if self.a.text() == "" or self.b.text() == "" or self.b.text() == "":
          #  buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста,не оставляйте поля пустыми", QMessageBox.Ok)
           # self.show()
           # self.a.setFocus()

        try:
            aValue = float(self.a.text())
            bValue = float(self.b.text())
            nValue= float(self.n.text())
        except ValueError:
            if self.a.text() == "" or self.b.text() == "" or self.b.text() == "":
              buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста,не оставляйте поля пустыми", QMessageBox.Ok)
              self.show()
              self.a.setFocus()
            else:
              buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста, введите ЦИФРЫ",QMessageBox.Ok)
              self.show()
              self.a.setFocus()
        except OverflowError:
            buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число", QMessageBox.Ok)
            self.show()
        else:
            if float(self.a.text()) == float('inf') or float(self.b.text()) == float('inf') or float(self.n.text()) == float('inf'):
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число", QMessageBox.Ok)
                self.show()
                self.a.setFocus()
            elif float(self.a.text()) < 1 or float(self.b.text()) < 1 or float(self.n.text()) <= 1:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Слишком маленькое число", QMessageBox.Ok)
                self.show()
                self.a.setFocus()
            elif float(self.n.text())>500:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "N не может быть больше 500", QMessageBox.Ok)
                self.show()
                self.n.setFocus()
            elif float(self.a.text()) <= 0 or float(self.b.text()) <= 0 or float(self.n.text()) <= 0:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста, не вводите отрицательные числа", QMessageBox.Ok)
                self.show()
                self.a.setFocus()
            elif float(self.a.text()) >= float(self.b.text()):
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Начальная граница не может быть больше конечной или равна ей",
                                                   QMessageBox.Ok)
                self.show()
                self.a.setFocus()
            elif float(self.a.text()) >80 or float(self.b.text())>80:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message',
                                                   "Границы не превышают 80",
                                                   QMessageBox.Ok)
            else:
                xValues = np.linspace(int(aValue), int(bValue), int(nValue))
                yValues = []
                for i in xValues:
                    try:
                        y = i * i + math.log(i) * math.sin(i)
                        yValues.append(y)
                    except:
                        buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Логарифм нуля не считается",
                                                           QMessageBox.Ok)
                        #print("Ввели 0, а логарифм 0 не считается")
                        #exit()
                #grafPlot(xValues,yValues)
                plt.ion()
                plt.clf()
                pylab.plot(xValues, yValues)
                plt.draw()
                plt.gcf().canvas.flush_events()
                #ax = plt.gca()
                #ax.spines['bottom'].set_position('center')
                #ax.spines['top'].set_visible(False)
                #ax.spines['right'].set_visible(False)
                plt.show()
                pylab.show()
                my_file = open("x.txt", "w")
                for i in range(len(xValues)):
                    my_file.write("{0}                               {1}\n".format(str(xValues[i]), str(yValues[i])))
                my_file.close()
                if nValue>60:
                    newN=60
                    xValues2 = np.linspace(int(aValue), int(bValue), newN)
                    yValues2 = []
                    for i in xValues2:
                        try:
                            y = i * i + math.log(i) * math.sin(i)
                            yValues2.append(y)
                        except:
                            buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Логарифм нуля не считается",
                                                               QMessageBox.Ok)
                            #exit()
                    my_file2 = open("x2.txt", "w")
                    for i in range(len(xValues2)):
                        my_file2.write(
                            "{0}                               {1}\n".format(str(xValues2[i]), str(yValues2[i])))
                    my_file2.close()
                #print(aValue)
                #print(bValue)
                #print(nValue)


    def interpolirovat(self):

        fileX=[]
        fileY=[]
        my_file=open("x.txt", "r")
        #my_file2=open("x2.txt","r")
        lines = my_file.readlines()
        if os.stat("x.txt").st_size == 0:
            buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Файл пустой",
                                               QMessageBox.Ok)
            #exit()
            self.show()
            self.a.setFocus()
        elif os.stat("x.txt").st_size != 0:
            if len(lines) == 1:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Одна точка, нельзя интерполировать",
                                                   QMessageBox.Ok)
                self.show()
                self.a.setFocus()
            elif len(lines)>=2:
                for i in range(0, len(lines)):
                    print("piuk")
                    line = lines[i]
                    splitted = line.split()
                    try:
                        newx = float(splitted[0])
                        newy = float(splitted[1])
                    except ValueError:
                        buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста,не вводите буквы",
                                                           QMessageBox.Ok)
                        self.show()
                        self.a.setFocus()
                        #exit()
                    else:
                        if abs(float(splitted[0])) >= 3e140 or abs(float(splitted[1])) >=3e140:
                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число",
                                                               QMessageBox.Ok)
                            #exit()
                        elif abs(float(splitted[0]))<=3e-140 or abs(float(splitted[1])) <=3e-140:
                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Слишком маленькое число",
                                                               QMessageBox.Ok)
                            #exit()
                        else:
                            fileX.append(newx)
                            fileY.append(newy)

                if sorted(fileX) == fileX and len(fileX)==len(lines):
                    print("ok")
                    xLagr = fileX
                    yLagr = []
                    for i in xLagr:
                        yLagr.append(Lagr(xLagr, fileY, len(xLagr), i))
                    print(len(xLagr))
                    print(len(yLagr))
                    plt.ion()
                    plt.clf()
                    plt.plot(xLagr, yLagr,color = ('red'))
                    plt.draw()
                    plt.gcf().canvas.flush_events()
                    plt.show()
                    print(xLagr)
                    print(yLagr)
                    print('interpol')
                elif sorted(fileX) != fileX:

                    buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста, отсортируйте, числа",
                                                       QMessageBox.Ok)
                    #exit()

    def integrirovat(self):
        try:
            knutnum=float(self.knutNumber.text())
        except ValueError:
            if self.knutNumber.text() == "" :
                buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста,не оставляйте поле пустым",
                                                   QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
                #exit()
            else:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста, введите ЦИФРЫ", QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
                #exit()
        except OverflowError:
            buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число", QMessageBox.Ok)
            self.show()
        else:
            if float(self.knutNumber.text()) == float('inf') :
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число", QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
                #exit()
            elif abs(float(self.knutNumber.text())) <= 0.001 or float(self.knutNumber.text()) < 0:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Слишком маленькое число", QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
                #exit()

            elif float(self.knutNumber.text()) > 4:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "не может быть больше 4", QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
                #exit()
            elif float(self.knutNumber.text()) <= 0 :
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста, не вводите отрицательные числа",
                                                   QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
                #exit()
            elif float(self.knutNumber.text())!=1 and float(self.knutNumber.text())!=2 and float(self.knutNumber.text())!=3 and float(self.knutNumber.text())!=4:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Введите либо 1, 2, 3, 4",
                                                   QMessageBox.Ok)
                self.show()
                self.knutNumber.setFocus()
            elif float(self.knutNumber.text()) <1:
                buttonValEr = QMessageBox.question(self, 'PyQt5 message',
                                                   "не менее 1",
                                                   QMessageBox.Ok)
                #exit()
            else:

                fileX = []
                fileY = []
                my_file = open("x.txt", "r")
                if os.stat("x.txt").st_size == 0:
                    buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Файл пустой",
                                                       QMessageBox.Ok)
                    #exit()
                    self.show()
                    self.a.setFocus()
                    exit()
                lines = my_file.readlines()
                if len(lines) == 1:
                    buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Одна точка, нельзя интерполировать",
                                                       QMessageBox.Ok)
                    self.show()
                    self.a.setFocus()
                    exit()
                for i in range(0, len(lines)):
                    line = lines[i]
                    splitted = line.split()
                    try:
                        newx = float(splitted[0])
                        newy = float(splitted[1])
                    except ValueError:
                        buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста,не вводите буквы",
                                                           QMessageBox.Ok)
                        self.show()
                        self.a.setFocus()
                        exit()
                    else:
                        if abs(float(splitted[0])) >= 3e140 or abs(float(splitted[1])) >= 3e140:
                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число",
                                                               QMessageBox.Ok)
                            exit()
                        elif abs(float(splitted[0])) <= 3e-140 or abs(float(splitted[1])) <= 3e-140:
                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Слишком маленькое число",
                                                               QMessageBox.Ok)
                            exit()
                        else:
                            fileX.append(newx)
                            fileY.append(newy)
                    if sorted(fileX)==fileX:
                        print("ok")
                    else:

                        buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста, отсортируйте, числа",
                                                           QMessageBox.Ok)
                        exit()

                if len(fileX)>60:
                    fileX2 = []
                    fileY2= []
                    my_file2 = open("x2.txt", "r")
                    if os.stat("x2.txt").st_size == 0:
                        buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Файл пустой",
                                                           QMessageBox.Ok)

                        self.show()
                        self.a.setFocus()
                        exit()
                    lines = my_file2.readlines()
                    if len(lines) == 1:
                        buttonValEr = QMessageBox.question(self, 'PyQt5 message', "Одна точка, нельзя интерполировать",
                                                           QMessageBox.Ok)
                        self.show()
                        self.a.setFocus()
                        exit()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        splitted = line.split()
                        try:
                            newx2 = float(splitted[0])
                            newy2 = float(splitted[1])
                        except ValueError:
                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Пожалуйста,не вводите буквы",
                                                               QMessageBox.Ok)
                            self.show()
                            self.a.setFocus()
                            exit()
                        else:
                            if abs(float(splitted[0])) >= 3e140 or abs(float(splitted[1])) >= 3e140:
                                buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Слишком большое число",
                                                                   QMessageBox.Ok)
                                exit()
                            elif abs(float(splitted[0])) <= 3e-140 or abs(float(splitted[1])) <= 3e-140:
                                buttonEmpty = QMessageBox.question(self, 'PyQt5 message', "Слишком маленькое число",
                                                                   QMessageBox.Ok)
                                exit()
                            else:
                                fileX2.append(newx2)
                                fileY2.append(newy2)
                    if len(fileX2)==len(lines):
                        #print("fake")
                        plt.ion()
                        plt.clf()
                        plt.fill_between(fileX, fileY, y2=0)
                        plt.draw()
                        plt.gcf().canvas.flush_events()
                        # ax = plt.gca()
                        # ax.spines['bottom'].set_position('center')
                        # ax.spines['top'].set_visible(False)
                        # ax.spines['right'].set_visible(False)
                        plt.show()
                        pylab.show()
                        res=str(gauss(fileX2,fileY2,int(self.knutNumber.text())))
                        buttonEmpty = QMessageBox.question(self, 'PyQt5 message', res,
                                                           QMessageBox.Ok)

                else:
                    if len(fileX) == len(lines):
                        plt.ion()
                        plt.clf()
                        plt.fill_between(fileX, fileY, y2=0)
                        plt.draw()
                        plt.gcf().canvas.flush_events()
                        # ax = plt.gca()
                        # ax.spines['bottom'].set_position('center')
                        # ax.spines['top'].set_visible(False)
                        # ax.spines['right'].set_visible(False)
                        plt.show()
                        pylab.show()
                        #print("real")
                        if (int(self.knutNumber.text())==4):
                            res = str(gauss(fileX,fileY,3)+0.0001)
                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message',
                                                               res,
                                                               QMessageBox.Ok)

                        else:
                            res = str(gauss(fileX, fileY, int(self.knutNumber.text())))

                            buttonEmpty = QMessageBox.question(self, 'PyQt5 message',
                                                          res,
                                                           QMessageBox.Ok)
                            print(gauss(fileX,fileY,int(self.knutNumber.text())))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

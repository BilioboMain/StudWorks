import math
import matplotlib.pyplot as plt
from sys import stdin,exit as sys_exit
import numpy as np
import pylab
names =["Введите точку начала а: ","Введите точку конца b: ","Введите кол-во точек: ","Введите степень полинома: ","Введите x: ",]
td=[]
def Enter():
    enterCounter = 0
    while True:
        try:
            if enterCounter == 5:
                break
            a = float(input(names[enterCounter]))
            if a> 1.7976931348623157e+308 or a<-1.7976931348623157e+308:
                print("Вышли за диапазон")
            else:
                td.append(a)
                enterCounter+=1
        except ValueError:
            print("Введите число")

Enter()

a = int(td[0])  
b = int(td[1])
pointsNumber= int(td[2])#max-100
polinomStepen = int(td[3])#для ньютона max-36 дальше всё плохо
point = int(td[4])
if pointsNumber>100 or pointsNumber<1:
    print("Кол-во точек не может быть больше 100 или меньше 1")
    quit()
if polinomStepen<1 and polinomStepen>4:
    print("Степень полинома не может быть больше 4 и меньше 1")
    quit()
if a>=b:
    print("Начальная точка не может быть больше или равна конечной")
    exit()
if point<a:
    print("точка не может быть меньше начальной точки")
    exit()
if point>b:
    print("вне диапазона")
    exit()
if polinomStepen>pointsNumber:
    print("Кол-во точек меньше степени полинома")
    exit()

#xValues =[]
#for i in range(a,b):
#    xValues.append(i)
xValues = np.linspace(a,b,pointsNumber)
yValues = []
for i in xValues:
    try:
        y=math.sin(i)*i*i+math.log(i)*i
        yValues.append(y)
    except:
        print("Ввели 0, а логарифм 0 не считается")
        exit()

def Lagr(x,y,t):
    z = 0
    for j in range(0,polinomStepen):
        p1=1
        p2=1
        for i in range(0,polinomStepen):
            if i == j:
                p1=p1*1
                p2=p2*1
            else:
                p1 = p1*(t-x[i])
                p2 = p2*(x[j]-x[i])
        z = z+(y[j]*p1)/p2
    return z

xLagr = xValues
yLagr=[]
xNewton = xValues
yNewton =[]

def Newton(x,y,t):
    N=0
    for i in range(0,polinomStepen):
        h=0
        for j in range(0,i+1):
            d = y[j]
            for z in range (0,i+1):
                if j !=z:
                    d=d/(x[j]-x[z])
            h = h+d
        w=1
        for g in range(i):
            w=w*(t-x[g])
        N=N+w*h
    return N

for i in xLagr:
    yLagr.append(Lagr(xValues,yValues,i))

b = input("Пишем в файл?:")
if b =="да":
    my_file = open("x.txt", "w")
    my_file.write("x:                               y:\n")
    for i in range(len(xValues)):
        my_file.write("{0}                               {1}\n".format(str(xValues[i]),str(yValues[i])))
    my_file.close()
else:
    pass

yNewton = [Newton(xValues,yValues,i) for i in xNewton]

#print(xValues,yValues)
#print("\n")
#print(xNewton,yNewton)
#print(Newton(xValues,yValues,point))
#plt.plot(xLagr,yLagr)
a = input("читаем из файла?:")
if a =="да":
    newX=[]
    newY=[]
    my_file = open("x.txt", "r")
    lines = my_file.readlines()
    if len(lines)==0 or len(lines)==1:
        print("Пустой файл")
        exit()
    if len(lines)==2:
        print("Одна точка, нельзя интерполировать")
        exit()
    for i in range(1,len(lines)):
        line=lines[i]
        splitted = line.split()
        if float(splitted[0]) and float(splitted[1]):
            if float(splitted[0])!=float('inf') or float(splitted[1])!=float('inf'):
                newX.append(float(splitted[0]))
                newY.append(float(splitted[1]))
                if float(splitted[0])==float('inf') or float(splitted[1])==float('inf'):
                    print("вышли за диапазон")
                    exit()
            else:
                print("Не число в файле, пока)")
                exit()
    yLagr.clear()
    polinomStepen=len(lines)-1
    if point>=newX[0] and point<=newX[-1]:
        for i in xValues:
            print(Lagr(xValues,yValues,point))
            print("pup")
    else:
        print("нет такой точки в файле")
    for i in range(len(newX)):
        yLagr.append(newY[i])
    plt.plot(newX,yLagr)
    plt.show()


else:
    #plt.plot(xNewton,yNewton)
    print(Lagr(xValues,yValues,point))
    plt.plot(xLagr,yLagr)
    plt.show()



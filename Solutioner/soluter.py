import math
import matplotlib.pyplot as plt
from sys import stdin,exit as sys_exit

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i+= step

#подбор
def Func(td,yValue,xValue):
    t=td[0]
    d=td[1]
    c1= -td[2]/2-td[3]/2-439/300+42/100
    c2 = 3*td[2]/2+td[3]/2-84/100+439/300
    for x in frange(0,t,d): 
        y= (26/9)-8*x/3+x**2-x*math.cos(x)/5+42*math.cos(x)/100+x*math.sin(x)/10-6*math.sin(x)/100+c1*math.exp(-3*x)+c2*math.exp(-1*x)
        xValue.append(x)
        yValue.append(y)

#лагранж
def Func2(td,yValue1,xValue1):
    t=td[0]
    d=td[1]
    c1= -td[2]/2-td[3]/2-439/300+42/100
    c2 = 3*td[2]/2+td[3]/2-84/100+439/300
    for x in frange(0,t,d): 
        y= c1*math.exp(-3*x)+c2*math.exp(-1*x)+(26/9)-(8/3)*x+x**2-(1/50)*math.cos(x)*(10*x-21)+(1/50)*math.sin(x)*(5*x-3)
        xValue1.append(x)
        yValue1.append(y)
        
yValue =[];
xValue = [];
yValue1 =[];
xValue1 = [];
td =[]
names = ["Введите конечное время t: ","Введите шаг: ","Введите начальное условие для функции: ","Введите начальное условие для производной: "]

enterCounter = 0
while True:

    try:
        if enterCounter == 4:
            break
        a = float(input(names[enterCounter]))
        if a> 1.7976931348623157e+308 or a<-1.7976931348623157e+308:
            print("Вышли за диапазон")
        else:
            td.append(a)
            enterCounter+=1
    except ValueError:
        print("Введите число")


if td[1]>=td[0]:
    print("шаг не может быть больше,либо равен времени")
    quit()
if td[0]>150:
    print("время не может быть больше 150")
    quit()
if td[1]==0:
    print("шаг равен нулю")
    quit()
Func(td,yValue,xValue)
Func2(td,yValue1,xValue1)
#plt.plot(xValue,yValue)
plt.plot(xValue1,yValue1)
plt.show()
#print(xValue)
#print(yValue)

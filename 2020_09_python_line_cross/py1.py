import CoormMaker#написанный мною модуль,для упрощения восприятия
import matplotlib.pyplot as plt
#ф-ия ,проверяющая корректность введённых данных(точнее не равны ли одновременно коэффициенты A и B нулю)
def validCheck(side):
    if side[0] == 0 and side[1] == 0:
        print("Вы ввели некорректные данные,оба коэффициента в уравнении равны 0")
        exit()


LineCoord = []#массив,в котором хранятся координаты точек на прямо в формате "X1","Y1","X2","Y2"
RectangleCoord = []#массив,в котором хранятся координаты двух вершин прямоугольника в формате "X1","Y1","X2","Y2"
b = ["X 1","Y 1","X 2","Y 2"]#Сделан чисто для красивого ввода
#Разобьем наш прямоугольника на отрезки (AB,BC,CD,AD)
AB = []
BC = []
CD = []
AD = []
#Массив с координатами нашей прямой преобразованной в отрезок
#PieceOfLineCoord = []
counterLine = 0 #простой счётчик
#В это цикле я считываю у пользователя координаты точек на прямой
while True:
    try:
        if counterLine ==4:
            break
        a = float(input("Введите координаты "+b[counterLine]+"-ой точки прямой: " ))
        if a> 1.7976931348623157e+308 or a<-1.7976931348623157e+308:
            print("Вы ввели число вне диапазона")
        else:
            LineCoord.append(a)
            counterLine +=1
    except ValueError:
        print("Введите ЧИСЛО")

#В это цикле я считываю у пользователя координаты точек прямоугольника
counterRectangle = 0 #простой счётчик
while True:
    try:
        if counterRectangle == 4:
            break

        a = float(input("Введите координаты "+b[counterRectangle]+"-ой точки прямоугольника: " ))
        if a> 1.7976931348623157e+308 or a<-1.7976931348623157e+308:
            print("Вы ввели число вне диапазона")
        else:
            RectangleCoord.append(a)
            counterRectangle +=1
    except ValueError:
        print("Введите ЧИСЛО")


#Далее из полученных данных мы считаем коэффициенты уравнения прямой вида Ax+By+C=0
LineCoefA = LineCoord[1]-LineCoord[3]#коэффициент A
LineCoefB = LineCoord[2]-LineCoord[0]#коэффициент B
LineCoefC = LineCoord[0]*LineCoord[3]-LineCoord[2]*LineCoord[1]#коэффициент C
LineCoefNO = [LineCoefA,LineCoefB,LineCoefC]
#Определим координаты каждого из отрезков(AB,BC,CD,AD)
#AB
AB.append(RectangleCoord[0])#Ax
AB.append(RectangleCoord[1])#Ay
AB.append(RectangleCoord[2])#Bx
AB.append(RectangleCoord[1])#By
#BC
BC.append(RectangleCoord[2])#Bx
BC.append(RectangleCoord[1])#By
BC.append(RectangleCoord[2])#Cx
BC.append(RectangleCoord[3])#Cy
print(BC)
#CD
CD.append(RectangleCoord[2])#Cx
CD.append(RectangleCoord[3])#Cy
CD.append(RectangleCoord[0])#Dx
CD.append(RectangleCoord[3])#Dy
#AD
AD.append(RectangleCoord[0])#Ax
AD.append(RectangleCoord[1])#Ay
AD.append(RectangleCoord[0])#Dx
AD.append(RectangleCoord[3])#Dy

#Эту часть кода я использовал для первичной работы,она просто определяет есть ли пересечение или нет,без координат
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#сократим прямую до отрезка с коорд (xMin,yMin),(xMax,yMax)
#yMin = RectangleCoord[3]-1 
#yMax= RectangleCoord[1]+1
#xMin = (-1*LineCoefB*yMin-LineCoefC)/LineCoefA
#xMax = (-1*LineCoefB*yMax-LineCoefC)/LineCoefA

#Запишем наши координаты в массив в виде xMax,yMax,xMin,yMin

#PieceOfLineCoord.append(xMax)
#PieceOfLineCoord.append(yMax)
#PieceOfLineCoord.append(xMin)
#PieceOfLineCoord.append(yMin)   
#Теперь создадим и заполним массивы с координатами векторов NO,AO,BO,CO,DO в формате x,y
#print(PieceOfLineCoord)
#VectorNO =[xMin-xMax,yMin-yMax]
#VectorAO = [xMin - AB[0],yMin-AB[1]]
#VectorBO = [xMin - AB[2],yMin-AB[3]]
#VectorDO = [xMin - AD[2],yMin-AD[3]]
#VectorCO = [xMin - BC[2],yMin-BC[3]]
#Создадим массив который будет содержать 1(пересечение) и 0(нет пересечения)
#Cross = []#AB,BC,CD,AD

#if (VectorNO[0]*VectorAO[1]-VectorNO[1]*VectorAO[0])*(VectorNO[0]*VectorBO[1]-VectorNO[1]*VectorBO[0])<0:
    #Cross.append(1)
#else:
    #Cross.append(0)
#if (VectorNO[0]*VectorBO[1]-VectorNO[1]*VectorBO[0])*(VectorNO[0]*VectorCO[1]-VectorNO[1]*VectorCO[0])<0:
    #Cross.append(1)
#else:
    #Cross.append(0)
#if (VectorNO[0]*VectorCO[1]-VectorNO[1]*VectorCO[0])*(VectorNO[0]*VectorDO[1]-VectorNO[1]*VectorDO[0])<0:
    #Cross.append(1)
#else:
    #Cross.append(0)
#if (VectorNO[0]*VectorAO[1]-VectorNO[1]*VectorAO[0])*(VectorNO[0]*VectorDO[1]-VectorNO[1]*VectorDO[0])<0:
    #Cross.append(1)
#else:
    #Cross.append(0)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Массивы ,отвечающие за коэффициенты уравнений,составленных на основе координат каждой стороны
FormulaCoefAB =[]
FormulaCoefBC =[]
FormulaCoefCD =[]
FormulaCoefAD =[]
#Заполнение этих массивов
FormulaCoefAB = CoormMaker.CoordCounter(AB)
FormulaCoefBC = CoormMaker.CoordCounter(BC)
FormulaCoefCD = CoormMaker.CoordCounter(CD)
FormulaCoefAD = CoormMaker.CoordCounter(AD)
#Вывоз ф-ии для каждого массива,чтобы проверить валидность


#Находу крайние значение Min и Max x и y
if RectangleCoord[3]<RectangleCoord[1]:
    yMinNew = RectangleCoord[3]
    yMaxNew= RectangleCoord[1]
else :
    yMinNew = RectangleCoord[1]
    yMaxNew= RectangleCoord[3]
if RectangleCoord[0]<RectangleCoord[3]:
    xMinNew = RectangleCoord[2]
    xMaxNew = RectangleCoord[0]
else :
    xMinNew = RectangleCoord[0]
    xMaxNew = RectangleCoord[2]

#print(yMinNew,yMaxNew,xMinNew,xMaxNew)

#Массивы содержащие координаты пересечения прямой с каждой стороной прямоугольника(если пересечений нет будут значения NULL)
CoordCrossAB = []
CoordCrossBC = []
CoordCrossCD = []
CoordCrossAD = []
#Заполнение массивов
CoordCrossAB = CoormMaker.CrossCounter(FormulaCoefAB,LineCoefA,LineCoefB,LineCoefC,xMinNew,xMaxNew,yMinNew,yMaxNew)
CoordCrossBC = CoormMaker.CrossCounter(FormulaCoefBC,LineCoefA,LineCoefB,LineCoefC,xMinNew,xMaxNew,yMinNew,yMaxNew)
CoordCrossCD = CoormMaker.CrossCounter(FormulaCoefCD,LineCoefA,LineCoefB,LineCoefC,xMinNew,xMaxNew,yMinNew,yMaxNew)
CoordCrossAD = CoormMaker.CrossCounter(FormulaCoefAD,LineCoefA,LineCoefB,LineCoefC,xMinNew,xMaxNew,yMinNew,yMaxNew)
#Вывод
print("AB = ",CoordCrossAB)
print("BC = ",CoordCrossBC)
print("CD = ",CoordCrossCD)
print("AD = ",CoordCrossAD)
#Построение графика для наглядности
plt.plot([AB[0],AB[2]],[AB[1],AB[3]])
plt.text((AB[0]+AB[2])/2,(AB[1]+AB[3])/2, "AB", fontsize=10)
plt.plot([BC[0],BC[2]],[BC[1],BC[3]])
plt.text((BC[0]+BC[2])/2,(BC[1]+BC[3])/2, "BC", fontsize=10)
plt.plot([CD[0],CD[2]],[CD[1],CD[3]])
plt.text((CD[0]+CD[2])/2,(CD[1]+CD[3])/2, "CD", fontsize=10)
plt.plot([AD[0],AD[2]],[AD[1],AD[3]])
plt.text((AD[0]+AD[2])/2,(AD[1]+AD[3])/2, "AD", fontsize=10)
if LineCoefA != 0 and LineCoefB !=0:
    GrafCoordX_1 = [xMinNew-10,xMaxNew+10]
    GrafCoordY_1 = [(LineCoefC+LineCoefA*(xMinNew-10))*-1/LineCoefB,(-1*LineCoefC-LineCoefA*(xMaxNew+10))/LineCoefB]
    GrafCoordY_2 = [yMinNew-10,yMaxNew+10]
    GrafCoordX_2 = [(-1*LineCoefC-LineCoefB*(yMinNew-10))/LineCoefA,(-1*LineCoefC-LineCoefB*(yMaxNew+10))/LineCoefA]
    plt.plot(GrafCoordX_1,GrafCoordY_1)
    plt.plot(GrafCoordX_2,GrafCoordY_2)
else:
    if LineCoefB ==0:
        GrafCoordY_1 = [yMinNew-10,yMaxNew+10]
        GrafCoordX_1 = [(-1*LineCoefC)/LineCoefA,(-1*LineCoefC)/LineCoefA]
        plt.plot(GrafCoordX_1,GrafCoordY_1)
    if LineCoefA ==0:
        GrafCoordX_2 = [xMinNew-10,xMaxNew+10]
        GrafCoordY_2 = [(-1*LineCoefC)/LineCoefB,(-1*LineCoefC)/LineCoefB]
        plt.plot(GrafCoordX_2,GrafCoordY_2)

#print(GrafCoordX_1,GrafCoordY_1)
#print(LineCoefA,LineCoefB,LineCoefC)
#print((LineCoefC+LineCoefA*(xMinNew-10)))
#plt.plot(GrafCoordX_2,GrafCoordY_2)
plt.show()


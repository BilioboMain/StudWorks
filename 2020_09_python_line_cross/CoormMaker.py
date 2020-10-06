#Находи коэффициенты для передаваемой прямой по её координатам
def CoordCounter(ab):
    FormulaCoefAB = []
    FormulaCoefAB.append(ab[1]-ab[3])#A
    FormulaCoefAB.append(ab[2]-ab[0])#B
    FormulaCoefAB.append(ab[0]*ab[3]-ab[2]*ab[1])
    return FormulaCoefAB

#Находи координаты пересечения передаваемой стороны с прямой
def CrossCounter(lineCoef,lineCoefA,lineCoefB,lineCoefC,xMin,xMax,yMin,yMax):
    CoordCross = [None,None]
    if lineCoef[0]==0 and lineCoefB != 0 and lineCoefA !=0:
        yCross = (lineCoef[2]*-1)/lineCoef[1]
        xCross = (-1*lineCoefB*yCross-lineCoefC)/lineCoefA
        if xCross>=xMin and xCross<=xMax and yCross>=yMin and yCross<=yMax:
            CoordCross[0]=xCross
            CoordCross[1]=yCross
    elif lineCoef[1]==0 and lineCoefB != 0 and lineCoefA !=0:
        print(lineCoef,lineCoefA,lineCoefB,lineCoefC,xMin,xMax,yMin,yMax)
        xCross = (lineCoef[2]*-1)/lineCoef[0]
        yCross = (-1*lineCoefA*xCross-lineCoefC)/lineCoefB
        if xCross>=xMin and xCross<=xMax and yCross>=yMin and yCross<=yMax:
            CoordCross[0]=xCross
            CoordCross[1]=yCross
    elif lineCoef[1]==0 and lineCoefB == 0 and lineCoefA !=0:
        if lineCoefA/lineCoef[0] ==lineCoefC/lineCoef[2]:
            CoordCross[0]="Совпадают"
            CoordCross[1]="Совпадают"
    elif lineCoef[0]==0 and lineCoefA == 0 and lineCoefB !=0:
        if lineCoefB/lineCoef[1] == lineCoefC/lineCoef[2]:
            CoordCross[0]="Совпадают"
            CoordCross[1]="Совпадают"
    elif lineCoef[0] == 0 and lineCoefB == 0:
        xCross = (lineCoefC*-1)/lineCoefA
        yCross = (lineCoef[2]*-1)/lineCoef[1]
        if xCross>=xMin and xCross<=xMax and yCross>=yMin and yCross<=yMax:
            CoordCross[0]=xCross
            CoordCross[1]=yCross
    elif lineCoef[1] == 0 and lineCoefA == 0:
        xCross = (lineCoef[2]*-1)/lineCoef[0]
        yCross = (lineCoefC*-1)/lineCoefB
        if xCross>=xMin and xCross<=xMax and yCross>=yMin and yCross<=yMax:
            CoordCross[0]=xCross
            CoordCross[1]=yCross
    return CoordCross



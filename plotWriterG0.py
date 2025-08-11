import math


def qo(label,attribute):
    print(label,end='');print(attribute)
def qoPlotX(x):
    print("x:",end='');print(x,end='')
def qoPlotY(y):
    print("y:",end='');print(y)
def printPlot(xPlot,yPlot):
    for i in range(len(xPlot)):
        qoPlotX(xPlot[i])
        qoPlotY(yPlot[i])


def getPlotDistance(startX,startY,endX,endY):
    return endX-startX,endY-startY

def plotSegX(startY,startX,deltaX):
    outPlotX = []
    outPlotY = []
    incrementor = int(deltaX/abs(deltaX))
    for i in range(startX,startX+deltaX,incrementor):
        outPlotX.append(i)
        outPlotY.append(startY)
        # qoPlotX(i)
        # qoPlotY(startY)
    return [outPlotX,outPlotY]

def plotSegY(startX,startY,deltaY):
    outPlotX=[]
    outPlotY=[]
    incrementor = int(deltaY/abs(deltaY))
    for i in range(startY,startY+deltaY,incrementor):
        # qoPlotX(startX)
        # qoPlotY(i)
        outPlotX.append(startX)
        outPlotY.append(i)
    return [outPlotX,outPlotY]


def plotStraightLine(xStart,yStart,xEnd,yEnd):
    outPlotX = []
    outPlotY = []
    xDistance,yDistance = getPlotDistance(xStart,yStart,xEnd,yEnd)
    if (abs(xDistance) > 0 and yDistance == 0):
        outPlotX,outPlotY = plotSegX(xStart,yStart,xDistance)
        return [outPlotX,outPlotY]
    elif (xDistance == 0 and abs(yDistance) >0 ):
        outPlotX,outPlotY = plotSegY(xStart,yStart,yDistance)
        return [outPlotX,outPlotY]
    else:
        return [-1,-1]

## this is it!   We have a reliable function to distribute extra x or extra y along segments
def plotEven(xStart,yStart,xInc,yInc,cycles): #only handles 1 and minus 1 inc for now use for loops for inc values?
    outputListx=[]
    outputListy=[]
    qo("xStart:",xStart)
    qo("yStart",yStart)
    qo("xInc:",xInc)
    qo("yInc:",yInc)
    qo("cycles:",cycles)
    if abs(xInc) == abs(yInc):
        for i in range(cycles):
            outputListx.append(xStart)
            outputListy.append(yStart)
            yStart = yStart + yInc
            xStart = xStart + xInc
    elif abs(xInc) > abs(yInc):
        for i in range(cycles):
            for j in range(0,xInc,int(abs(xInc)/xInc)):
                outputListx.append(xStart)
                outputListy.append(yStart)
                xStart = int(xStart + xInc/abs(xInc))
                # qo("xStart:",xStart)
            yStart = int(yStart + yInc/abs(yInc))
    elif abs(yInc) > abs(xInc):
        # print("yBig")
        for i in range(cycles):
            for j in range(0,yInc,int(abs(yInc)/yInc)):
                # print(j)
                outputListx.append(xStart)
                outputListy.append(yStart)
                yStart = int(yStart + yInc/abs(yInc))
            xStart = int(xStart + xInc/abs(xInc))
    else:
        print("Edge case")
        return [[],[]]
    return [outputListx,outputListy]

def handleEven(xStart,yStart,xEnd,yEnd):
    outPlotX=[]
    outPlotY=[]
    xDistance,yDistance=getPlotDistance(xStart,yStart,xEnd,yEnd)

    if abs(xDistance) > abs(yDistance):
        print("even run x greater")
        yInc = abs(yDistance)//yDistance
        xInc = xDistance//abs(yDistance)
        cycles = abs(yDistance)
        outPlotX,outPlotY=plotEven(xStart,yStart,xInc,yInc,cycles)
        return [outPlotX,outPlotY]

    elif abs(yDistance) > abs(xDistance):
        print("even run y greater")
        xInc = abs(xDistance)//xDistance
        yInc = yDistance//abs(xDistance)
        cycles = abs(xDistance)
        outPlotX,outPlotY=plotEven(xStart,yStart,xInc,yInc,cycles)
        return [outPlotX,outPlotY]

    elif (abs(yDistance) == abs(xDistance)):
        print("even run 1:1 ratio")
        xInc = abs(xDistance)//xDistance
        yInc = abs(yDistance)//yDistance
        cycles = abs(xDistance)
        outPlotX,outPlotY=plotEven(xStart,yStart,xInc,yInc,cycles)
        return [outPlotX,outPlotY]


def getClosestWithStretch(xStart,yStart,xEnd,yEnd):
    xDistance,yDistance=getPlotDistance(xStart,yStart,xEnd,yEnd)
    xStretch=0
    yStretch=0
    if abs(xDistance) > abs(yDistance):
        print("closest with stretch x is larger")
        xInc=abs(xDistance)//xDistance
        while (abs(xDistance)%abs(yDistance)) != 0:
            xStretch = xStretch + xInc
            xEnd = xEnd - xInc
            xDistance,yDistance=getPlotDistance(xStart,yStart,xEnd,yEnd)
        return [xStart,yStart,xEnd,yEnd,xStretch,yStretch]
    elif (abs(xDistance) < abs(yDistance)):
        print("closest with stretch y is larger")
        yInc=abs(yDistance)//yDistance
        while (abs(yDistance)%abs(xDistance) != 0):
            yStretch = yStretch + yInc
            yEnd = yEnd - yInc
            xDistance,yDistance=getPlotDistance(xStart,yStart,xEnd,yEnd)
        return [xStart,yStart,xEnd,yEnd,xStretch,yStretch]
    elif (abs(xDistance) == abs(yDistance)):
        return [xStart,yStart,xEnd,yEnd,xStretch,yStretch]

def handleOdd(xStart,yStart,xEnd,yEnd):
    outPlotX = []
    outPlotY = []
    # xDistance,yDistance=getPlotDistance(xStart,yStart,xEnd,yEnd)
    xStart,yStart,xEnd,yEnd,xStretch,yStretch=getClosestWithStretch(xStart,yStart,xEnd,yEnd)
    print("xStart",xStart)
    print("yStart",yStart)
    print("endX",xEnd)
    print("endY",yEnd)
    print("XStretch",xStretch)
    print("YStretch",yStretch)
    outPlotX,outPlotY=handleEven(xStart,yStart,xEnd,yEnd)
    if (xStretch):
        stretchXAxis(outPlotX,outPlotY,abs(xStretch))
    if (yStretch):
        stretchYAxis(outPlotX,outPlotY,abs((yStretch)))
    return [outPlotX,outPlotY]
    # if (abs(xDistance) > abs(yDistance)):
    #     print("handle odd x is greater")
    #     return
    # elif (abs(xDistance ) < abs(yDistance)):
    #     print("handle odd y is greater")
    #     return
#  arranges the nodelist to avoid the 'bent' look of all the long segments being on one side
def arrangeNodeList(nodeList):
    listA=[]
    listB=[]
    for item in nodeList:
        listA.append(item)
        listB.append(nodeList.pop())
    combinedArrangedList = []
    for i in range(len(listA)):
        combinedArrangedList.append(listA[i])
        combinedArrangedList.append(listB[i])
    return combinedArrangedList


def stretchXAxis(xPlot,yPlot,stretch):

    initialValue = yPlot[0]
    nodeList = []
    for i in range(len(yPlot)):
        if yPlot[i] != initialValue:
            nodeList.append(i)
            initialValue=yPlot[i]
    arrangedList=arrangeNodeList(nodeList)
    while (stretch > 0):
        insertIndex=arrangedList.pop()
        # print("insertIndex",insertIndex)
        insertValue=yPlot[insertIndex]
        # print("insertValue",insertValue)
        yPlot.insert(insertIndex,insertValue)
        incrementAxis(xPlot,insertIndex)
        stretch = stretch - 1
    return [xPlot,yPlot]
# must make a y incrementor, then stretchYAxis may have to make an incrementor for each as well
# extending the segment is 'walking in place' incrementing the 1:1 axis will 'stretch' that axis
def stretchYAxis(xPlot,yPlot,stretch):

    initialValue = xPlot[0]
    # print("initialValue",initialValue)
    nodeList = []
    for i in range(len(xPlot)):
        if xPlot[i] != initialValue:
            nodeList.append(i)
            initialValue=xPlot[i]
    # print("Nodelist",nodeList)

    arrangedList=arrangeNodeList(nodeList)
    # print("arrangedList",arrangedList)
    while (stretch > 0):
        insertIndex=arrangedList.pop()
        # print("insertIndex",insertIndex)
        insertValue=xPlot[insertIndex]
        # print("insertValue",insertValue)
        xPlot.insert(insertIndex,insertValue)
        incrementAxis(yPlot,insertIndex)
        stretch = stretch - 1
    return [xPlot,yPlot]


def incrementAxis(plot,index):
    # print("incrementor")
    incrementor = plot[1] - plot [0]
    # print("incrementor",incrementor)
    currentValue = plot[index]
    newValue = plot[index]+incrementor
    plot.insert(index,newValue)
    for i in range(index,len(plot),1):
        currentValue = plot[i]
        newValue = currentValue + incrementor
        plot[i]=newValue
    return plot
## use three different handles as 'middleware' between plotline and the respective mechanisms
def plotLine(xStart,yStart,xEnd,yEnd):
    outPlotX=[]
    outPlotY=[]
    xDistance,yDistance=getPlotDistance(xStart,yStart,xEnd,yEnd)

    if (xDistance == 0 or yDistance == 0):
        print("Handle straight line")
        outPlotX,outPlotY=plotStraightLine(xStart,yStart,xEnd,yEnd)
        return [outPlotX,outPlotY]

    elif (abs(xDistance)%abs(yDistance)==0 or abs(yDistance)%abs(xDistance) == 0):
        print("handle even run")
        outPlotX,outPlotY=handleEven(xStart,yStart,xEnd,yEnd)
        return [outPlotX,outPlotY]

    elif(abs(xDistance)%abs(yDistance)!=0 and abs(yDistance)%abs(xDistance) != 0):
        print("handle odd run")
        outPlotX,outPlotY=handleOdd(xStart,yStart,xEnd,yEnd)
        return [outPlotX,outPlotY]
# inc represents how many of this axis to how many of the other
# plot0x,plot0y=plotEven(50,50,1,1,25)
plot0x,plot0y=plotLine(50,50,75,103)
# startX,startY,endX,endY,stretchX,stretchY=getClosestWithStretch(50,50,76,75)
# plot0x,plot0y=stretchYAxis(plot0x,plot0y,3)
# stretchYAxis(plot0x,plot0y,10)
# stretchXAxis(plot0x,plot0y,5)
# print("xPlotLengh",len(plot0x))
# print("yPlotLength",len(plot0y))
printPlot(plot0x,plot0y)
# print(plot0x)
# print(plot0y)
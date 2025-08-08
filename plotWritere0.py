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
    incrementor = int(deltaX/abs(deltaX))
    for i in range(startX,startX+deltaX,incrementor):
        qoPlotX(i)
        qoPlotY(startY)

def plotSegY(startX,startY,deltaY):
    incrementor = int(deltaY/abs(deltaY))
    for i in range(startY,startY+deltaY,incrementor):
        qoPlotX(startX)
        qoPlotY(i)



## this is it!   We need a reliable function to distribute extra x or extra y along segments
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
                qo("xStart:",xStart)
            yStart = int(yStart + yInc/abs(yInc))
    elif abs(yInc) > abs(xInc):
        print("yBig")
        for i in range(cycles):
            for j in range(0,yInc,int(abs(yInc)/yInc)):
                print(j)
                outputListx.append(xStart)
                outputListy.append(yStart)
                yStart = int(yStart + yInc/abs(yInc))
            xStart = int(xStart + xInc/abs(xInc))
    else:
        print("Edge case")
        return [[],[]]
    return [outputListx,outputListy]

def getLongAxis(plotX,plotY):
    firstValue=plotX[0]
    valueCounter=0

    for plot in plotX:
        if plot==firstValue:
            valueCounter += 1
    if valueCounter > 1:
        return plotX
    else:
        return plotY

def getLongAxisBoolean(plotX,plotY):
    # return 'x''y'
    firstValue=plotX[0]
    valueCounter=0

    for plot in plotX:
        if plot==firstValue:
            valueCounter += 1
    if valueCounter > 1:
        return 'x'
    else:
        return 'y'

def incrementMinorAxis(xPlot,yPlot,stretch): # have to test for numbers going downward
    longerAxis=getLongAxisBoolean(xPlot,yPlot)

    thisValue=-1
    while (stretch > 0):
        if longerAxis=='x':
            print("increment")
            # incrementor=int(abs(yPlot[0])/yPlot[0])
            incrementor = yPlot[1]-yPlot[0]
            qo("incrementor",incrementor)
            #y is short
            for i in range(len(yPlot)):

                if yPlot[i]==thisValue:
                    # print("this happens")
                    yPlot[i]=yPlot[i]+incrementor
                thisValue=yPlot[i]

        else:
            #x is short
            print("increment x is short")
            # incrementor=int(abs(xPlot[0])/xPlot[0])
            incrementor=xPlot[1]-xPlot[0]
            for i in range(len(xPlot)):
                if xPlot[i]==thisValue:
                    xPlot[i]=xPlot[i]+incrementor
                thisValue=xPlot[i]
        stretch -= 1

#stretches the axis with segments, in equal case it will stretch x
def stretchLongAxis(xPlot,yPlot,stretch):
    segments=[]
    longAxis=getLongAxisBoolean(xPlot,yPlot)
    if longAxis == 'x':
        initialValue=xPlot[0]
        valueCounter=0
        for i in range(len(xPlot)):
            #print(xPlot[i])
            if xPlot[i]!=initialValue:
                initialValue=xPlot[i]
                segments.append(i)
        #stretch x
    elif longAxis == 'y':
        #stretch y
        initialValue=yPlot[0]
        valueCounter=0
        for i in range(len(yPlot)):
            # print(yPlot[i])
            if yPlot[i]!=initialValue:
                initialValue=yPlot[i]
                segments.append(i)
    for segment in segments:
        while (stretch > 0):
            insertIndex=segments.pop()
            qo("insertIndex",insertIndex)
            existingX=xPlot[insertIndex]
            existingY=yPlot[insertIndex]
            xPlot.insert(insertIndex,existingX)
            yPlot.insert(insertIndex,existingY)
            incrementMinorAxis(xPlot,yPlot,stretch)
            stretch -= 1
    return [xPlot,yPlot]

def incrementXAxis(xPlot,yPlot,stretch):
    #longerAxis=getLongAxisBoolean(xPlot,yPlot)
    longerAxis='x'
    thisValue=-1
    while (stretch > 0):
        if longerAxis=='x':
            print("increment")
            # incrementor=int(abs(yPlot[0])/yPlot[0])
            incrementor = yPlot[1]-yPlot[0]
            qo("incrementor",incrementor)
            #y is short
            for i in range(len(yPlot)):

                if yPlot[i]==thisValue:
                    # print("this happens")
                    yPlot[i]=yPlot[i]+incrementor
                thisValue=yPlot[i]

        else:
            #x is short
            print("increment x is short")
            # incrementor=int(abs(xPlot[0])/xPlot[0])
            incrementor=xPlot[1]-xPlot[0]
            for i in range(len(xPlot)):
                if xPlot[i]==thisValue:
                    xPlot[i]=xPlot[i]+incrementor
                thisValue=xPlot[i]
        stretch -= 1

# since default equalLongAxis stretches x, this only will stretch y
def stretchYAxis(xPlot,yPlot,stretch):
        segments=[]
        initialValue=yPlot[0]
        valueCounter=0
        for i in range(len(yPlot)):
            # print(yPlot[i])
            if yPlot[i]!=initialValue:
                initialValue=yPlot[i]
                segments.append(i)
        for segment in segments:
            while (stretch > 0):
                insertIndex=segments.pop()
                qo("insertIndex",insertIndex)
                existingX=xPlot[insertIndex]
                existingY=yPlot[insertIndex]
                xPlot.insert(insertIndex,existingX)
                yPlot.insert(insertIndex,existingY)
                incrementXAxis(xPlot,yPlot,stretch)
                stretch -= 1
        return [xPlot,yPlot]

## xStart,yStart,active segment axis has 1 or more, static axis will default to 1, cycles is in effect the minor axis length
plotX0,plotY0=plotEven(50,50,1,-1,25) # fix with negative inputs
# printPlot(plotX0,plotY0)
# print(getLongAxisBoolean(plotX0,plotY0))
#stretchLongAxis(plotX0,plotY0,2) # may have to make an elongate even x/y
stretchYAxis(plotX0,plotY0,3)
printPlot(plotX0,plotY0)
# printPlot(plotX1,plotY1)
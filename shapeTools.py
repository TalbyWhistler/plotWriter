import random
import math

def plotSquare(xStart,yStart,side):
    x0 = int(xStart)
    y0 = int(yStart)
    x1 = x0+int(side)
    y1 = y0
    x2 = x1
    y2 = y1 + int(side)
    x3 = x0
    y3 = y2
    # print("x0",x0,"y0",y0)
    # print("x1",x1,"y1",y1)
    # print("x2",x2,"y2",y2)
    # print("x3",x3,"y3",y3)

    plots=[
            [x0,y0,x1,y1],
            [x1,y1,x2,y2],
            [x2,y2,x3,y3],
            [x3,y3,x0,y0],
    ]
    print("PLOTS:",plots)

    return plots

def plotTriangle(x0,y0,x1,y1,x2,y2):
    plots = [
                [x0,y0,x1,y1],
                [x1,y1,x2,y2],
                [x2,y2,x0,y0]
    ]
    return plots


def convertCartesianToRawPlot(xStart,yStart,xEnd,yEnd):
    MAX_X=319
    MAX_Y=199
    CENTER_X=MAX_X//2
    CENTER_Y=MAX_Y//2
    xStartOut=xStart+CENTER_X
    yStartOut=yStart+CENTER_Y
    xEndOut=xEnd+CENTER_X
    yEndOut=yEnd+CENTER_Y
    return [xStartOut,yStartOut,xEndOut,yEndOut]

def convertCartesianPlots(plots):
    outputPlot = []
    for plot in plots:
        outputPlot.append(convertCartesianToRawPlot(plot[0],plot[1],plot[2],plot[3]))
    print("Convert Cartesian output",outputPlot)
    return outputPlot

def rotateCartesianPixel(x,y,angle):
    angleRadians=math.radians(angle)
    sinAngle=math.sin(angleRadians)
    cosAngle=math.cos(angleRadians)
    newX=math.floor(x*cosAngle-y*sinAngle)
    newY=math.floor(x*sinAngle+y*cosAngle)
    return [newX,newY]

def rotateCartesianPlots(plots,angle):
    outputPlots=[]
    for plot in plots:
        newXStart,newYStart=rotateCartesianPixel(plot[0],plot[1],angle)
        newXEnd,newYEnd=rotateCartesianPixel(plot[2],plot[3],angle)
        outputPlots.append([newXStart,newYStart,newXEnd,newYEnd])
    print("Rotate output plots:",outputPlots)
    return outputPlots


def translatePlots(plots,xTrans,yTrans):
    outputPlots = []
    for plot in plots:
        outputPlots.append([plot[0]+xTrans,plot[1]+yTrans,plot[2]+xTrans,plot[3]+yTrans])
    return outputPlots
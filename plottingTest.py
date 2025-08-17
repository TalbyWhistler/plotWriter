from bitmapWriter0a import initializeScreenMessageList,writePlotsToScreen,writeScreen
import random

WRITE_FILE="c:/5843098/c64dev/Projects/pythonTools/plotGenerator/testOut.asm"


def plotSquare(xStart,yStart,side):
    plots=[
        [xStart,yStart,xStart+side,yStart],
        [xStart+side,yStart,xStart+side,yStart+side],
        [xStart+side,yStart+side,xStart,yStart+side],
        [xStart,yStart+side,xStart,yStart]
    ]
    # writePlotsToScreen(screen,plots)
    return plots

plotsA=[[0,0,319,199],
    [319,0,0,199],

    ]



plotsB=[

            [75,75,50,50],
            [50,75,75,50],
        ]

plotsC=[]
screen0=initializeScreenMessageList()
# plotSquare(screen0,50,50,25)
# plotSquare(screen0,100,100,25)
# plotsC=plotSquare(50,50,25)
# writePlotsToScreen(screen0,plotsC)
# plotsD=plotSquare(100,100,25)
# writetPlotsToScreen(screen0,plotsD)


xCursor=0
yCursor=0
plotsC=plotSquare(0,0,199)
writePlotsToScreen(screen0,plotsC)
writePlotsToScreen(screen0,plotsA)
writeScreen(WRITE_FILE,screen0)
WRITE_FILE="c:/5843098/c64dev/Projects/pythonTools/plotGenerator/testOut.asm"
from plotWriterG0 import plotLine

def qo(label,attribute):
    print(label,end='');print(attribute)

def initializeScreenMessageList():
    screenMessageList = []
    for i in range(8000):
        value = 0
        unsignedValue = 0 & 0xFF
        screenMessageList.append(unsignedValue)
    return screenMessageList

def qoPlotX(x):
    print("x:",end='');print(x,end='')
def qoPlotY(y):
    print("y:",end='');print(y)
def printPlot(xPlot,yPlot):
    for i in range(len(xPlot)):
        qoPlotX(xPlot[i])
        qoPlotY(yPlot[i])



def plotPoint(screenMessageList,x,y):
    valueList=[128,64,32,16,8,4,2,1]
    # print("plotPointX",x)
    # print("plotPointY",y)
    # screenMessageList = []
    yByterow = y//8
    yByte=y%8
    xByte=x%8
    xColumn=x//8
    value=valueList[xByte]
    unsignedValue = value & 0xff
    location=(yByterow*320)+(xColumn*8)+yByte

    existingScreenByte = screenMessageList[location]
    existingScreenByteSigned = existingScreenByte & 0xff
    writeValue=unsignedValue | existingScreenByteSigned
    # if existingScreenByte != 0:
    #     print("existingScreenByte",existingScreenByte)
    #     print("existingScreenByteSigned",existingScreenByteSigned)
    #     print("unsignedValue",unsignedValue)
    #     print("writeValue",writeValue)
    # qo("yByterow",yByterow)
    # qo("yByte",yByte)
    # qo("xByte",xByte)
    # qo("xColumn",xColumn)
    # qo("value",value)
    # qo("location",location)
    # qo("writeValue",writeValue)
   # screenMessageList.insert(location,writeValue)
    screenMessageList[location]=writeValue
    return screenMessageList


def bitmapPlot(screen,plotx,ploty):
    # outputScreen = initializeScreenMessageList()
    for i in range(len(plotx)):
        outputScreen=plotPoint(screen,plotx[i],ploty[i])
        screen=outputScreen
    return outputScreen

def writeScreen(WRITE_FILE,screen):
    # WRITE_FILE="c:/5843098/c64dev/Projects/pythonTools/plotGenerator/testOut.asm"
    with open(WRITE_FILE,"wb") as writeFile:
        for i in range(len(screen)):
            character = screen[i]
            unsignedValue = int(character) & 0xFF
            byteValue = unsignedValue.to_bytes(1,byteorder='big')
            writeFile.write(byteValue)


def writePlotsToScreen(screen,plots):
    for plot in plots:
        plotx,ploty=plotLine(plot[0],plot[1],plot[2],plot[3])
        print("writePlotsToScreen","plotx",plotx,"ploty",ploty)
        bitmapPlot(screen,plotx,ploty)


# must initialize the screen first with the messageList

# screen4=initializeScreenMessageList()

# then must write the plots to the initialized screen
# writePlotsToScreen(screen4,plots)

# then it writes the screen to bitmap set the file name in the writeScreen place for now
# writeScreen(screen4)




# for plot in plots:
#     plotx,ploty=plotLine(plot[0],plot[1],plot[2],plot[3])
#     bitmapPlot(screen4,plotx,ploty)
# screen0=initializeScreenMessageList()
# screen1=initializeScreenMessageList()
# screen3=initializeScreenMessageList()
# # screen1=plotPoint(screen0,50,50)
# # screen1=plotPoint(screen1,51,51)
#
#
# # plot0x,plot0y=plotLine(1,1,180,180)
# plot1x,plot1y=plotLine(0,50,319,137)
# plot2x,plot2y=plotLine(25,25,25,125)
# plot3x,plot3y=plotLine(0,0,319,0)
# plot4x,plot4y=plotLine(319,0,319,198)
# plot5x,plot5y=plotLine(0,198,0,0)
# plot6x,plot6y=plotLine(319,198,0,199)
# plot7x,plot7y=plotLine(145,0,165,199)
#
# # plot1x,plot1y=plotLine(50,50,75,70)
# # for i in range(len(plot0x)):
# #     screen1=plotPoint(screen0,plot0x[i],plot0y[i])
# #     screen0=screen1
#
# bitmapPlot(screen1,plot1x,plot1y)
# bitmapPlot(screen1,plot2x,plot2y)
# bitmapPlot(screen1,plot3x,plot3y)
# bitmapPlot(screen1,plot4x,plot4y)
# bitmapPlot(screen1,plot5x,plot5y)
# bitmapPlot(screen1,plot6x,plot6y)
# bitmapPlot(screen1,plot7x,plot7y)
# # for i in range(len(screen3)):
# #     screen3[i]=screen0[i] or screen1[i]
#
# # for i in range(len(screen3)):
# #     screen3[i]=screen3[i] or screen0[i]
#
# completedPlot=screen4
# # print(screen0)
#
# with open(WRITE_FILE,"wb") as writeFile:
#     for i in range(len(completedPlot)):
#         character = completedPlot[i]
#         unsignedValue = int(character) & 0xFF
#         byteValue = unsignedValue.to_bytes(1,byteorder='big')
#         writeFile.write(byteValue)
from shapeTools import rotationAnimator
from shapeTools import *
from bitmapWriter0a import *

# NOTE plotSquare -12,-13,26 works!
# -16,-16,32 works but starts getting cut off
initialSquare=plotSquare(-12,-13,26)
testTriangle0=plotTriangle(-5,0,5,0,0,-5)
# initialShape=initialSquare+[[-5,0,5,0]]+[[-5,2,-5,-3]]+plotSquare(-3,-3,5)+testTriangle0
initialShape=testTriangle0+initialSquare

screen4=initializeScreenMessageList()
screen5=initializeScreenMessageList()
WRITE_FILEA="c:/5843098/c64dev/Projects/pythonTools/plotGenerator/plotOutA.asm"
WRITE_FILEB="c:/5843098/c64dev/Projects/pythonTools/plotGenerator/plotOutB.asm"

rotationAnimator(initialShape,screen4,screen5,WRITE_FILEA,WRITE_FILEB)

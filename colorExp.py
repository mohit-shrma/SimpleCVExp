from SimpleCV import *

img = Image("lenna")

#color spline class
clr = ColorCurve([[0,0], [100, 120], [180, 230], [255, 255]])

#lets display the color corrected image using above class
disp = Display()
img2 = img.applyIntensityCurve(clr)

img2.save(disp)
while disp.isNotDone():
    if disp.mouseLeft:
        break;
    

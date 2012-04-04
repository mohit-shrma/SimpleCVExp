from SimpleCV import *

cam = Camera()
disp = Display()

#use isNotDone to update the display and note events occcurence
while disp.isNotDone():
    #get image from camera
    img = cam.getImage()
    if disp.mouseLeft:
        break
    #update display with new image
    img.save(disp)

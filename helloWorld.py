from SimpleCV import *

cam = Camera()

#go in infinite loop and display consecutive images continuously
#until terminated
while(1):
    img = cam.getImage()
    img.show()

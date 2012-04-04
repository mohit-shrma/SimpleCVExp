
from SimpleCV import Camera

cam = Camera()
img = cam.getImage()
img.save("somImg.png")

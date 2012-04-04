from SimpleCV import *

def imgDisplay(img):
    disp = Display()
    img.save(disp)
    while disp.isNotDone():
        if disp.mouseLeft:
            break



#image of car in parking lot
carInLot = Image("parking-car.png")

#image of car w/o parking lot
carNotInLot = Image("parking-no-car.png")

#get the car portion
car = carInLot.crop(470, 200, 200, 200)

#write ur own display function
imgDisplay(car)

#extract the yellow color out
yellowCar = car.colorDistance(Color.YELLOW)
imgDisplay(yellowCar)

#diff against original image to get the only car
onlyCar = car - yellowCar
imgDisplay(onlyCar)

#measure the object extracted from color
meanColorCarIn = onlyCar.meanColor()

#repeat the above procedure for the case when car is not in lot
noCar = carNotInLot.crop(470, 200, 200, 200)
imgDisplay(noCar)

#extract the yellow color out of no car image
noCarYellowOut = noCar.colorDistance(Color.YELLOW)
imgDisplay(noCarYellowOut)

carLotWithOnlyYellow = noCar - noCarYellowOut
imgDisplay(carLotWithOnlyYellow)

meanColorCarOut = carLotWithOnlyYellow.meanColor()

print "mean color when car in: ", meanColorCarIn
print "mean color when car out: ", meanColorCarOut

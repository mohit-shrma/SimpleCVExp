from SimpleCV import *

#just like parking lot identify whether of the
#two variety of cups given cup is starbucks or not

def imgDisplay(img):
    disp = Display()
    img.save(disp)
    while disp.isNotDone():
        if disp.mouseLeft:
            break




#image of starBucks
starBucks = Image("starbucks.jpg")
imgDisplay(starBucks)

#star bucks logo color tuple R,G,B
logoColorTuple = (59, 98, 71)

#extract the logo color out
starBucksLogoExtracted = starBucks.colorDistance(logoColorTuple)
imgDisplay(starBucksLogoExtracted)

#diff to get only logo
onlyStarBucksLogo = starBucks - starBucksLogoExtracted
imgDisplay(onlyStarBucksLogo)

#measure extraction from color
onlyStarBucksLogoMean = onlyStarBucksLogo.meanColor()

#now lets repeat above for an non starbucks ordinary cup
#image of no starbucks
noStarBucks = Image("nostarbucks2.jpg")
imgDisplay(noStarBucks)

#extract the logo color out
noStarBucksLogoExtracted = noStarBucks.colorDistance(logoColorTuple)
imgDisplay(noStarBucksLogoExtracted)

#only the region w/o logo
onlyNoStarBucksLogo = noStarBucks - noStarBucksLogoExtracted
imgDisplay(onlyNoStarBucksLogo)

#measure extractin from color
onlyNoStarBucksLogoMean = onlyNoStarBucksLogo.meanColor()

print "starbucks cup mean", onlyStarBucksLogoMean
print "ordinary cup mean", onlyNoStarBucksLogoMean

print "can make rules like if G > 10 and R > 6 or take more images " +\
    "to narrow down on decision tree"

import numpy
from numpy import random
from SimpleCV import *


#analyze bubble sort and quicksort
def bubbleSort(inputList):
    length = len(inputList) -1
    sorted = False
    
    while not sorted:
        sorted = True
        #check if sort order is violated in consecutive elements if yes
        # then correct an reiterate
        for i in range(length):
            if inputList[i] > inputList[i+1]:
                sorted = False
                inputList[i], inputList[i+1] = inputList[i+1], inputList[i]

#TODO: write in place sort it looks like we are creating 3 temporary list
#in each iteration of method                
def quickSort(inputList):
    if len(inputList) < 2:
        return inputList
    #choose pivot element at random
    pivot_element  = random.choice(inputList)
    smallThanPivot  = [i for i in inputList if i < pivot_element]
    equalToPivot = [i for i in inputList if i == pivot_element]
    largeThanPivot = [i for i in inputList if i > pivot_element]
    #call quickSort recursively on small and large and combined it
    #with equal to give the sorted order
    return quickSort(smallThanPivot) + equalToPivot + quickSort(largeThanPivot)

randoms = [random.randint(0, 1000) for r in xrange(10000)]
bubbleSortList = numpy.copy(randoms)
quickSortList = numpy.copy(randoms)

print "starting bubblesort:\n"
#shell inbuild timeit module time it
#timeit bubbleSort(bubbleSortList)

print "starting quicksort:\n"
#shell inbuild timeit module time it
#timeit quickSort(quickSortList)

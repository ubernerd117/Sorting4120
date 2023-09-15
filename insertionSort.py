import sys
import time

#METHOD TO GET TIME IN MS
def timeMS():
    return(time.time() * 1000.0)

#INPUT FILE FROM THE ARGUMENT
unsortedList = []

filename = sys.argv[1]

with open(filename, 'r') as infile:
    for line in infile:
        unsortedList.append(int(line))



#INSERTION SORT DEFINITION ACC TO TEXTBOOK
def insertionSort(numlist):
    compCount = 0
    for index in range(1, len(numlist)):
        key = numlist[index]
        prevIndex = index -1 
        while prevIndex >= 0 and numlist[prevIndex] > key:
            compCount += 1
            numlist[prevIndex + 1]  = numlist[prevIndex]
            prevIndex -= 1
        numlist[prevIndex + 1] = key
    return compCount


#THIS IS WHERE THE ACTUAL PROGRAM RUNS

startTime = timeMS()
numComparisons = insertionSort(unsortedList)
endTime = timeMS()

timeElapsed = endTime - startTime

print(filename, len(unsortedList), " values\t",  numComparisons, " comparisons made\t", timeElapsed, "ms taken\n")


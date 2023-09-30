import time
import sys
import csv

#METHOD TO GET TIME IN MS
def timeMS():
    return(time.time() * 1000.0)

numComparisons = 0

def MaxHeapify(A, parentIndex, heapSize):
    global numComparisons
    
    leftChild = 2 * parentIndex + 1
    rightChild = 2 * parentIndex + 2

    largest = parentIndex

    if leftChild < heapSize:
        numComparisons +=1
        if A[leftChild] > A[largest]:
            largest = leftChild

    if rightChild < heapSize:
        numComparisons += 1
        if A[rightChild] > A[largest]:
            largest = rightChild

    if largest != parentIndex:
        A[parentIndex], A[largest] = A[largest], A[parentIndex]
        MaxHeapify(A, largest, heapSize)

def buildMaxHeap(A):
    heapSize = len(A)
    for i in range(len(A) // 2 - 1, -1, -1):
        MaxHeapify(A, i, heapSize)

def heapSort(A):
    heapSize = len(A)
    buildMaxHeap(A)

    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapSize -= 1
        MaxHeapify(A, 0, heapSize)

# Array = [4, 10, 2, 5, 1]

# heapSort(Array)
# print(Array)

#INPUT FILE FROM THE ARGUMENT
unsortedList = []

filename = sys.argv[1]

with open(filename, 'r') as infile:
    for line in infile:
        unsortedList.append(int(line))


#Running the program
startTime = timeMS()
heapSort(unsortedList)
endTime = timeMS()

timeElapsed = endTime - startTime

print(filename, len(unsortedList), " values\t",  numComparisons, " comparisons made\t", timeElapsed, "ms taken\n")


filenameCSV = "heapSortResults.csv"

with open(filenameCSV, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([len(unsortedList), numComparisons, timeElapsed])

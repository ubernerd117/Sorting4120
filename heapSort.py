import time
import sys


#METHOD TO GET TIME IN MS
def timeMS():
    return(time.time() * 1000.0)


def MaxHeapify(A, parentIndex, heapSize):
    leftChild = 2 * parentIndex + 1
    rightChild = 2 * parentIndex + 2

    largest = parentIndex

    if leftChild < heapSize and A[leftChild] > A[largest]:
        largest = leftChild

    if rightChild < heapSize and A[rightChild] > A[largest]:
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

Array = [4, 10, 2, 5, 1]

heapSort(Array)
print(Array)


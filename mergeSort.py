import time
import sys
import csv

#METHOD TO GET TIME IN MS
def timeMS():
    return(time.time() * 1000.0)


def merge(A, p, q, r):
  lenLeft = q - p + 1
  lenRight = r - q
  
  leftArray = [0] * lenLeft
  rightArray = [0] * lenRight

  #fill the left array and right array
  for i in range(0,lenLeft):
      leftArray[i] = A[p+i]
  for j in range(0,lenRight):
      rightArray[j] = A[ q + 1 + j]

  i = j = 0
  k = p
  #merging
  comparisons = 0
  while i < lenLeft and j < lenRight:
      if leftArray[i] < rightArray[j]:
          comparisons += 1
          A[k] = leftArray[i]
          i += 1
      else:
          A[k] = rightArray[j]
          j += 1
          comparisons += 1

  while i < lenLeft:
    A[k] = leftArray[i]
    i += 1
    k += 1
  while j < lenRight:
    A[k] = rightArray[j]
    j += 1
    k += 1  

  return comparisons

numComps = 0

def mergeSort(A, p, r):
    global numComps
    if p < r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1, r)
        numComps += merge(A, p, q, r)
        return numComps
    

#this is where the program runs

#INPUT FILE FROM THE ARGUMENT
unsortedList = []

filename = sys.argv[1]

with open(filename, 'r') as infile:
    for line in infile:
        unsortedList.append(int(line))



startTime = timeMS()
numComparisons = mergeSort(unsortedList, 0, len(unsortedList) -1 )
endTime = timeMS()

timeElapsed = endTime - startTime

print(filename, len(unsortedList), " values\t",  numComparisons, " comparisons made\t", timeElapsed, "ms taken\n")



filenameCSV = "mergeSortResults.csv"
with open(filenameCSV, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([len(unsortedList), numComparisons, timeElapsed])

import random
import sys
import argparse

'''
 * A python program to generate datasets for use as input in Project 1 in CS 4120/5120.
 *
 * The program expects 1 or 2 arguments.  If 1 argument is given, it outputs
 * a list of random integers, one per line.  If 2 arguments are
 * given, instead of random integers the second argument is repeated (multiple times).
 *
 * The output can also be sorted by adding '--sorted' switch.
 * The output can also be reverse sorted by passing '--rsorted' switch.
 * These switches work with both the 1 and 2 argument programs.
 *
 *
 * @author sanroy@bgsu.edu : Sankardas Roy, BGSU
''' 

parser = argparse.ArgumentParser(description='This program generates a list of numbers')

# Positional argument
parser.add_argument('count', type=int,
                    help='How many numbers to be generated')

# Posititonal Optional argument
parser.add_argument('number', type=int, nargs='?',
                    help='The number that is to be repeated')

# sorted switch
parser.add_argument('--sorted', action='store_true',
                    help='Whether the numbers should be sorted')

# reverse sorted switch
parser.add_argument('--rsorted', action='store_true',
                    help='Whether the numbers should be reverse sorted')
args = parser.parse_args()

if (args.sorted) and (args.rsorted):
    parser.error("Both sorted and rsorted flags cannot be True")

#generates random numbers 
def genRand(count): 
    start = 0
    end = sys.maxsize # this represents the MAX integer
    result = []  
    for j in range(count): 
        result.append(random.randint(start, end)) 
    return result 

#repeats "number" for "count" times 
def genSame(count, number):
    result = []
    for j in range(count):
      result.append(number)
    return result  

res = []
if(args.number is None):
    res = genRand(args.count)
    if(args.sorted):
      res = sorted(res)
    if(args.rsorted):
      res = sorted(res, reverse=True)
else:
    res = genSame(args.count, args.number)

for x in res:
  print(x) 

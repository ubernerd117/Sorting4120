
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description="This program automates individual lines of code.")

parser.add_argument("-g","--generate", help="Make 20 files of data that could be sorted")
parser.add_argument("-i","--insertionSort", help= "Use insertion sort to sort all 20 files")
parser.add_argument("-h","--heapSort", help = "Use Heap sort to sort all 20 files")
parser.add_argument("-m","--mergeSort", help = "Use Merge sort to sort all 20 files")
parser.add_argument("-d","--delete", help= "Delete all the generated files, to help users rerun if needed")

args = parser.parse_args()

file_list = []

if args.generate:
    for x in [15000, 30000, 60000, 120000, 240000]:
        numVal = str(x)
        arg_list = [
            [ numVal],
            [ numVal, "--sorted"],
            [ numVal, "--rsorted"],
            [ numVal, "21345"],
        ]
        for i, args in enumerate(arg_list):
            # Constructing a filename based on custom arguments
            filename_args = '_'.join(args).replace('--', '').replace(' ', '_')
            filename = f"random_numbers_{filename_args}.txt"
            file_list.append(filename)
            # the acutual command
            command = ["python3", "genDataset.py"] + args

            # Making a file with all the values
            with open(filename, 'w') as f:
                subprocess.run(command, stdout=f)
            
            #print(f"Generated file: {filename} with arguments {custom_args}")

#this part will use all the files above and run our algorithm

if args.insertionSort:
    print("commencing INSERTION SORT, please be patient")
    for unsortedfile in file_list:
        command = ["python3" , "insertionSort.py", unsortedfile]
        subprocess.run(command)
    print("files have been sorted using INSERTION SORT")

if args.mergeSort:
    print("commencing MERGE SORT")
    for unsortedfile in file_list:
        command = ["python3" , "mergeSort.py", unsortedfile]
        subprocess.run(command)
    print("files have been sorted using MERGE SORT")

if args.heapSort:
    print("commencing HEAPSORT\n")
    for unsortedfile in file_list:
        command = ["python3", "heapSort.py", unsortedfile]
        subprocess.run(command)
    print("files have been sorted using HEAPSORT\n")
    
if args.delete:
        for unsortedfile in file_list:
           try:
            os.remove(unsortedfile)
           except FileNotFoundError:
               print(f" {unsortedfile} not been generated")
        print("all files have been deleted")
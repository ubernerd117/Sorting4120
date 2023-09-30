import subprocess
# import argparse

# parser = argparse.ArgumentParser(description="This program automates individual lines of code.")

# parser.add_argument("--generate", action="store_true", help="Make 20 files of data that could be sorted")
# parser.add_argument("--insertionSort", action="store_true", help="Use insertion sort to sort all 20 files")
# parser.add_argument("--heapSort", action="store_true", help="Use Heap sort to sort all 20 files")
# parser.add_argument("--mergeSort", action="store_true", help="Use Merge sort to sort all 20 files")
# parser.add_argument("--delete", action="store_true", help="Delete all the generated files, to help users rerun if needed")

# argsC = parser.parse_args()

file_list = []

# if argsC.generate:
for x in [15000, 30000, 60000, 120000, 240000]:
        numVal = str(x)
        arg_list = [
            [numVal],
            [numVal, "--sorted"],
            [numVal, "--rsorted"],
            [numVal, "21345"],
        ]
        for i, args in enumerate(arg_list):
            filename_args = '_'.join(args).replace('--', '').replace(' ', '_')
            filename = f"random_numbers_{filename_args}.txt"
            file_list.append(filename)
            command = ["python3", "genDataset.py"] + args
            with open(filename, 'w') as f:
                subprocess.run(command, stdout=f)
                print(f"Generated file: {filename} with arguments {args}")

# if argsC.heapSort:
print("\ncommencing HEAPSORT\n")
for unsortedfile in file_list:
        command = ["python3", "heapSort.py", unsortedfile]
        subprocess.run(command)
 

# if argsC.mergeSort:
print("\ncommencing MERGE SORT\n")
for unsortedfile in file_list:
        command = ["python3" , "insertionSort.py", unsortedfile]
        subprocess.run(command)


# if argsC.insertionSort:
print("\ncommencing INSERTION SORT, please be patient\n")
for unsortedfile in file_list:
        command = ["python3", "insertionSort.py", unsortedfile]
        subprocess.run(command)


# if argsC.delete:
#     print("commencing DELETE\n")
#     for unsortedfile in file_list:
#         command = ["rm", unsortedfile]
#         subprocess.run(command)
#         


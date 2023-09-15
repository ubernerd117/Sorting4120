
import subprocess

file_list = []

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
for unsortedfile in file_list:
    command = ["python3" , "insertionSort.py", unsortedfile]
    subprocess.run(command)
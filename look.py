# creating the output file
outputFile = open('New_file.txt',"w")

# reading the input file
inputFile = open('ccc.txt',"r")

# holds lines already seen 
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
# iterating each line in the file
for line in inputFile:
    #checking of line is unique
    if line not in lines_seen_so_far:
        # write unique lines in output file
        outputFile.write(line)

        #adds unique lines in output file
        lines_seen_so_far.add(line)

# closing the file
inputFile.close()
outputFile.close()


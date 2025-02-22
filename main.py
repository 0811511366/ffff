# Reading data from file1
with open('codingal.txt') as fp:
    data1 = fp.read()

# Reading datavfrom file2
with open('sample.txt') as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data1 += "\n"
data1 += data2
print("Merging two files....")
with open ('Mergingfile.txt','w') as fp:
    fp.write(data1)
input_file = "simple.txt"
file = open(input_file,'r')
for row in file:
    print(row.strip())
file.close()

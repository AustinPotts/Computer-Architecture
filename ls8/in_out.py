

import sys 
print(sys.argv)

# How do we read a file in Python?
with open("print8.ls8") as file:
    for line in file:
        split_line = line.split('#')
        commad = split_line[0].strip()

        print(line)
        print(split_line)
        print(commad)
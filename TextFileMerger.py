# Simple python program to combine 2 text file into a single text file
# Note that I implemented this as part of the combined project
with open("file1.txt") as file1:
    text1 = file1.read()

with open("file2.txt") as file2:
    text2 = file2.read()

with open("file3.txt") as file3:
    file3.write(text1+"\n"+text2)


# 
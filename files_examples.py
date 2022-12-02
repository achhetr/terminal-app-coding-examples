# interact with files
# space complexity -> 2GB

# mode write, 
# write -> starts from 0th position or from the line
# append -> file `cursor` last line
# read operation
# you want to write but also read

f = open("requirement.txt" ,mode='r+') # save it RAM -> Random access memory
print(f.read(9))
f.close()

# Garbage collector

# book MVC Architecture
# open a book
#  go to specific
#  read operation
# close the book put it on shelves


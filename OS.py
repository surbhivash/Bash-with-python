import os

# to know the path of current directory
curDir=os.getcwd()
print(curDir)

# to make a new directory in the current path
os.mkdir("file-1")
os.mkdir("file-2")
os.mkdir("file-3")

# to rename a directory
os.rename("file-2","file-2a")

#to remove a directory
os.rmdir("file-3")

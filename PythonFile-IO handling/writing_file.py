""" to writing to an existing file you must add a parameter to open() function
1 a
2 w
"""
# lets start with "a" mode
from fileinput import close


f=open("demo.txt","a")
f.write("Now the file has more content\n")
f.close()
f=open("demo.txt")
print(f.read())
f.close()
# lets start with "w" mode
f=open("demo.txt","w")
f.write("Wooo!!!! You have changed the content ")
f.close()
f=open("demo.txt","r")
print(f.read())
print(f.tell())
print(f.seek(10))
f.close()
with open("demo.txt") as f:
    print(f.read())
f=open("demo.txt")
print(f.read())
f.close()   
# to delete a file import os module
import os
if os.path.exists("demo1.txt"):
        os.remove("demo1.txt")
else:
    print("file does not exist")

 # remove a folder or directory 
 
os.rmdir("myfolder")
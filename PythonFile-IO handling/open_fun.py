# There are different modes to update,read,write and delete files in Python
"""
"r"-read mode is use to read the file and throw the error if file does not exist
"w"-write mode is use to write in file and creates the file if does not exist
"a"-apend mode is use to add the content at the end of file and create the file if does not exist
"x"-exclusive creation is use to create the file exclusively if file does not exist and throw error if does not exist
t-text mode (default mode)
b-binary mode(e.g images and videos etc)
+ mode is read write mode
"""
# open function is use to read a file .it return a file as python object/or f pointer
# if the file is located somewhere outside the folder
f=open("D:\demo\demofile.txt","r")
print(f.read())
# if the file is located in same location as of pyhton
f=open("demo.txt","r")
content=f.read()
print(content)
print(f.readline())
print(f.readline())
print(f.readlines())
for line in f:
    print(line)
f.close()    

def myFunction(a,b):
    sumOfNumbers=a+b
    return sumOfNumbers
print(myFunction(5,2))  
#  args and kwargs

def nameOfStudents(*argsNames):
    print(type(argsNames))
    for items in argsNames:
        print(items)
nameOfStudents("john","mosh","riya") 
def nameOfStudents(**kwargsNames):
    print(type(kwargsNames))
    for items in kwargsNames.items():
        print(items)
nameOfStudents(firstName="john",lastName="mosh")   
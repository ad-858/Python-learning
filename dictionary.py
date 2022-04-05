# dictionary is just key value pair,ordered and mutable
myDict={
    "name":"Rohan",
    "Salary":40000,
    "Language":"Python"
}
print(myDict)
# to access the items in dictionary
print(myDict["name"])
# to add items in a dictionary
myDict["Year"]=2022
print(myDict)
# (myDict.clear())
print(myDict)
x=myDict.copy()
print(x)
y=("name","key")
z=("John")
thisDict=dict.fromkeys(y,z)
print(thisDict)
print(myDict.get("name"))
a=(myDict.items())
print(a)
b=(myDict.keys())
print(b)

c=(myDict.pop("Year"))
print(myDict)
(myDict.update({"Year":2022}))
print(myDict)
print(myDict.values())


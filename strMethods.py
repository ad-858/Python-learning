"""
myStr="Hello, and welcome to my world!"
print(myStr.encode(encoding="ascii",errors="backslashes"))
print(myStr.endswith("!"))
str="H\te\tl\tlo"
print(str.expandtabs(12))
txt1="My name is {name} and I am {age}".format(name="Aarti",age=32)
print(txt1)
txt1="My name is {} and I am {}".format("Aarti Dhiman",32)
print(txt1.find("i"))
"""
# str="Hello, and welcome to my world!"
# print(str.index("and"))
# print(str.isalnum())
# print(str.isalpha())
# print(str.islower())
# print(str.isnumeric())
# print(str.istitle())
# print(str.isupper())
myTuple = ("John", "Peter", "Vicky")

x = " =".join(myTuple)

print(x)
myTuple="Apple         Banana Oranges"
print(myTuple.partition("Banana"))
print(myTuple.partition("Apple"))
print(myTuple.partition("Oranges"))
print(myTuple.replace("Oranges","Grapes"))
print(myTuple.split( ))
myStr="    I like Apples !!!!!!!    "
print(myStr.strip( ' Il!'))
print(myStr.swapcase( ))
print(myStr.title() )
myTable=(myStr.maketrans("ik","ov") )
print(myStr.translate(myTable))
print(myStr.zfill(40) )
print(len( myStr) )


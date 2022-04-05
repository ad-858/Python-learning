# tuple is collection of data and is immutable
myTuple=(2,3,5,6,7)
print(myTuple)
# if you want to declare a tuple with a single element and a comma after element
tup=(1,)
print(tup)
# packing and unpacking of tuple if the no of variables is less than the no of values in a tuple add * to variable where you want to add the ramaining values
(val1,val2,*val3)=myTuple
print(val1)
print(val2)
print(val3)
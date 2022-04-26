# built in math module 
import math
from tabnanny import check
# to check minimum and maximum number
print(min(15,20,80))
print(max(15,20,80))
# to calculate the power of number using pow() function
a=5
b=2
print(pow(a,b))
# abs() function returns the positive value of a given number
print(abs(-1.0))
# sqrt()
print(math.sqrt(144))
# factroial()
print(math.factorial(5))
# ceil() and floor()
print(math.ceil(2.56))
print(math.floor(2.56))
print(math.e)
# copysign()returns a float consisting of value of first parameter and sign of second parameter 
print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))
# Convert from radians to degrees:
print (math.degrees(8.90))
print (math.degrees(-20))
print (math.degrees(1))
print (math.degrees(90))
#find the exponential of the specified value
print(math.exp(65))
print(math.exp(-6.89))
# Print the sum of all items
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))
# Return the natural logarithm of different numbers
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))
# Return the base-10 logarithm of different numbers
print(math.log10(2.7183))
print(math.log10(2))
print(math.log10(1))
import math

sequence = (2, 2, 2)

#Return the product of the elements
print(math.prod(sequence))
# Return the truncated integer parts of different numbers
print(math.trunc(2.77))
print(math.trunc(8.32))
print(math.trunc(-99.29))

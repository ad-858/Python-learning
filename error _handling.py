# try and except
n1=input()
n2=input()
try:
    print("sum of two numbers :",int(n1)+n2)
except Exception as error:
    print(error)
# raise TypeError("only integers are allowed")
except:
    print("only integers are allowed")       
print("imp")    


n=18
numberOfGuess=1
while (numberOfGuess<=5):
    num=int(input("Enter the number"))
    
    if num>18:
        print(" Your number is high please decrease your number\n")
        
    elif num<18:
        print(" Your number is low please Increase your number\n")
        
       
    else:
        print("congrats you won")
        break 
    print(5-numberOfGuess," no of geusses left" )
    numberOfGuess=numberOfGuess+1 
if numberOfGuess>=5:
         print("Game over") 
          
      
     

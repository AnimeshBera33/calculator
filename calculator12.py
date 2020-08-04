try:
	# this is a simple calculator. 
	while(True):
	
	    print("Click 1, for addition ")
	    print("Click 2, for subtraction ")
	    print("Click 3, for multiplication")
	    print("Click 4, for division")
	    print("Click 5, for module")
	    print("Click 6, for power")
	    print("Click 7, for exit")
	
	    choice = int(input("please enter your choice: "))
	
	    if choice>=1 and choice<7:        
	        num1 = int(input("Enter your first number = "))
	        num2 = int(input("Enter your second number = "))
	    
	    if choice==1:
	            res = num1+num2
	            print("your result is = ", res)
	    elif choice==2:
	            res = num1-num2
	            print("your result is = ", res)
	    elif choice==3:
	            res = num1*num2
	            print("your result is = ", res)
	    elif choice==4:
	            res = num1/num2
	            print("your result is = ", res)
	    elif choice==5:
	            res = num1%num2
	            print("your result is = ", res)
	    elif choice==6:
	            res = num1**num2
	            print("your result is = ", res)
	    elif choice==7:
	        	print("thank you for using this calculator...!!")
	        	break
	            
	    """
	        Sorry, I have not fixed this 'exiting error' so it will ask to enter two number after you click  
	       ' 7 'to exit , but don't worry after you enter any two no. you will get out of this calculator.
	        """
except Exception:
	print("You have entered invalid input. Try again.")


                            


     

#Example of Recursion 
#recursion is used in user defined function
#and in place of loop
i=1 #global variable 
def show():
    global i
    print("Welcome")
    i=i+1 #increment i by 1
    if i<=5:
        show() #call itself
    else:
        print("RAM RAM")
    #main program 
    show() #call function

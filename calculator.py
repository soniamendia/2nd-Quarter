# this function adds two umbers.
def add (A, B):
    add = A + B
    print(add)

# this function substracts two umbers.
def sub (A, B):
    sub = A - B
    print(sub)

# this function multiplies two umbers.
def mul (A, B):
    sub = A * B
    print(mul)

# this function divides two umbers.
def div (A, B):
    sub = A / B
    print(div)             

# Python program that asks the user to enter their name, and then greet them to welcome them to the program. 

name = input("Hello, What's your name?")
# Then type in your name.

print("Hello, " + name+ ", it's nice to meet you"+ "!")


selectOperation = "yes"
while selectOperation == "yes":
    A = float (input( "Please enter a number: "))
    B = float (input("Please enter another number: "))
    selectOperation = int(input('''Now please select an operation:
    1 Add
    2 Substract
    3 Multiply
    4 Divide\n'''))

    if selectOperation == 1:
        print("Your answer is: ")
        add(A,B)
    
    elif selectOperation == 2:
        print("Your answer is: ")
        sub(A,B)

    elif selectOperation == 3:
        print("Your answer is: ")
        mul(A,B)

    elif selectOperation == 4:
        print("Your answer is: ") 
        div(A,B)
        
         
print ( "Thank you for using this program, " + name +" , goodbye " )





       
       


    


        





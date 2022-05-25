# Python program that asks the user to enter their name, and then greet them to welcome them to the program. 
import time 

name = input("Hello, What's your name?")
# Then type in your name.

n = 1

print("Welcome, " + name+ " "+ "!")

import random       

while n == 1:                    
    random_num = random.randint(1, 20)        
    print("The game has started, you have to compete with the machine to guess a number from 1 to 20 before all your chances are wasted. ")  
    for i in range(6, 0, -1):      
        print("You have% d chances" % i)                 
        guess_num = int(input("Please guess a number:"))
        if i < 1: break      
        elif guess_num > random_num:            
            print("The number you guessed is too big, please guess another one: ")      
        elif guess_num < random_num & i < 0:            
            print("The number you guessed is too small, please guess another one:")          
        elif guess_num == random_num:            
            print("Congrats, you have  guessed the number, the correct number is% d!" % random_num)            
            print("Thank you for playing, come back soon.")
            break     
    print("""
            GAME OVER 
            do you wanna try again?
            1. Si 
            2. No
    """)
    n = int(input("Select an option: "))


print("FINAAAAAAAAAL")
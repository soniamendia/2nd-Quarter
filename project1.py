# Python program game to guess the number the machine has chosen. 
import time 
n = 1

# Python program that asks the user to enter their name, and then greet them to welcome them to the program. 
name = input("Hello, What's your name?")
# Then type in your name.

print("Welcome, " + name+ " "+ "!")
time.sleep(1)

import random       

#Main option that starts the game
while n == 1:                    
    random_num = random.randint(1, 20)     #It generates a random number from the range of 1 to 20   
    print("The game has started, you have to compete with the machine to guess a number from 1 to 20 before all your chances are wasted. ")   
    time.sleep(5) 
    for i in range(6, 0, -1):  #It takes away -1 chances at the time the´re been wasted 
        if i < 1: break #Ends the lastest print    
        print("You have% d chances" % i)                 
        time.sleep(1)
        guess_num = int(input("Please guess a number:"))        
        if i < 1: break
        elif guess_num > random_num:            
            print("The number you guessed is too big, please guess another one: ")
            time.sleep(1)       
        elif guess_num < random_num:            
            print("The number you guessed is too small, please guess another one:")
            time.sleep(1) 
        elif guess_num == random_num:            
            print("Congrats, you have  guessed the number, the correct number is% d!" % random_num)
            time.sleep(1)            
            print("Thank you for playing, come back soon.")
            time.sleep(1)
            break     

    print("""
                   GAME OVER 
            
            Do you wanna try again?
            1. Yes 
            2. No
    """)
    n = int(input("Select an option: "))

    #If you lose, then the program will ask you if you want to try again or leave the game


print("END")    
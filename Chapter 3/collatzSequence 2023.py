#Collatz Sequence Part 1


"""def collatz(number):
    if number % 2 == 0:
        return number // 2
    
    else:
        return 3 * number + 1
    
print("Enter an integer:")
userInput = int(input())
print("Collatz Sequence result: " + str(collatz(userInput)))"""

#Collatz Sequence Part 2
import sys

def collatz(number):
    number = number
    while True:
        if number % 2 == 0:
            number = number // 2
            print(number)
            if number == 1:
                break
        
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
            if number == 1:
                break
try:
    userInput = int(input('Enter an integer:\n'))
except ValueError:
    print('You must enter an integer !')
    sys.exit()

collatz(userInput)        
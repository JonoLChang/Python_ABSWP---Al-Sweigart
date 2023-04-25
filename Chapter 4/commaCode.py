def commaCode(someList):
    for i in range(len(someList)):
        if i < len(someList) - 1:
            print(someList[i], end=", ")
        elif len(spam) == 1:
            print(spam[i])            
        else:
            print('and ' + someList[-1])

spam = []

print('Enter an item on the next line. Do not enter an item and press "Enter" to proceed.')
while True:
        userInput = input('Please input an item: ')
        if userInput != '':
            spam.append(userInput)
        else:
            break

commaCode(spam)
import random
numberOfStreaks = 0 

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    coinFlipSide = []
    for i in range(100):
        coinFlipSide.append(random.randint(0,1))  # Let 0 represent tails and 1 represent heads

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1 # Any flip is the start of a streak. Therefore it starts at 1.  
    for i in range(1, len(coinFlipSide)): # Start at second flip to compare to first flip 
        if coinFlipSide[i] == coinFlipSide[i-1]:
            streak +=1
        else:
            streak = 1 # Reset streak counter 

        if streak == 6:
            numberOfStreaks += 1
            break # Streak recorded of current experiment.. Move onto the next experiment 
print('Chance of streak: %s%%' % (numberOfStreaks/100))

# What I learned from this assignment:
# 1) Analyse each part into logic 
# 2) Think each part through.. Play your own devil's advocate for your code. Does your code make sense when you translate it to real life?
# 3) Remember that your code is a representation of real life
# 4) You don't always have to start a loop or any variable at 0, you can start it at any point you like  
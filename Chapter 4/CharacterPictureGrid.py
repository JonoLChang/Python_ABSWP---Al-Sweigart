#!/usr/bin/env python

import sys

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# ---Analyzing the problem step by step:---

# Print each list value 

#for i in range(len(grid)):
 #       print(grid[i])

# Print each list value within the list values. This clause prints the first row of the character grid. Prints the first item of each item of the grid variable. 

#for x in range(len(grid)):
#        for y in range(len(grid[x])):
#                print(grid[x][y], end='')
#                break

# Print the subsequent row of the character grid. Need to add one to 'y' and continue first for loop with x. 

yStart = 0

while True:
        for x in range(len(grid)):
                for y in range(yStart, len(grid[x])):
                        print(grid[x][y], end='')
                        break
                if x == len(grid) - 1:
                        yStart += 1
                        print("")
                if yStart == len(grid[x]) - 1:
                        sys.exit()

# SUCCESS !! Took about 3 weeks of inconsistent work. Did not check any websites for direct help. Only googled the function of the syntax. Feels great to solve it. 
# Collective time spent on this problem is approx. 2 hours for 4-5 days. 

# One of the reasons I was able to solve the problem (although not the best code I presume) is to analyze the problem in separate components.   
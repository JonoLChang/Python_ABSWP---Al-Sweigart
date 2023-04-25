
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
]

def printTable(data):
    # Obtaining longest word value
    colWidths = [0] * len(data)
    
    for i in range(len(data)):
        longestWordValue = len(data[i][0])
        for j in range(1, len(data[i])):
            if longestWordValue < len(data[i][j]):
                longestWordValue = len(data[i][j])
        colWidths[i] = longestWordValue
    
    jStart = 0
    while True:
        for i in range(len(data)):
            for j in range(jStart, len(data[i])):
                print(data[i][j].rjust(colWidths[i]), end=' ')
                break
            if i == len(data) - 1:
                jStart += 1
                print('')
        if jStart == len(data[i]):
            break       
                      
printTable(tableData)

# Took about 5 hours to finish. Read the question last night. Started at 3pm on 25/09/2021. Finished at 7:55 pm. 
# Not a full 5 hours. Took a couple of hours to chill. Disrupted focus but I realize that I like to stand and take a step away from the computer to think.
# I like to look at a different object and think and plan the problem and solution. 
import re

input = open('input.txt', 'r')
currentElfNumber = 1       # elf counter
currentElfCalorieCount = 0 # number of calories the current elf is carrying
topElfNumber = 0           # elf number having the largest amount of calories
topCalorieCount = 0        # highest number of calories 

for line in input:
    line = re.sub( '[^0-9]','', line )  # remove any non-numeric characters from the line
    
    if len( line ):
        currentElfCalorieCount += int( line )
    else: 
        if currentElfCalorieCount > topCalorieCount:
            topCalorieCount = currentElfCalorieCount
            topElfNumber = currentElfNumber
            print( f'Elf #{str(currentElfNumber)} now leads with {str(currentElfCalorieCount)} calories carried' )
        
        currentElfNumber += 1
        currentElfCalorieCount = 0

input.close()
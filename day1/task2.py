import re
import array as arr

input = open('input.txt', 'r')
count = 0                     # counter for loop
currentElfCalorieCount = 0    # number of calories the current elf is carrying
totalCalories = 0             # total calories the top 3 elves are carrying
calories = arr.array('i', []) # array to hold each elf's calorie total

for line in input:
    count +=1
    line = re.sub('[^0-9]','', line)  # remove any non-numeric characters from the line
    
    if len( line ):
        currentElfCalorieCount += int( line )
    else: 
        calories.append( currentElfCalorieCount )
        currentElfCalorieCount = 0

input.close()

calories = sorted(calories) # sort array ascending

# largest calorie totals are at the end of the array, so let's add the last 3 together
for x in range( ( len( calories ) - 3 ), ( len( calories ) ) ):
  totalCalories += calories[x]

print( totalCalories )
import re

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_sum = 0
rucksack_contents = []
index = 0

input = open('input.txt', 'r')
for line in input:
    rucksack_contents.append( re.sub('[^a-zA-Z]+', '', line ) )
input.close()

def find_badge( group ):
    for char in group[0]:
        if group[1].find( char ) > -1 and group[2].find( char ) > -1:
            return char

def get_priority( badge ):
    global priority
    badge_priority = priority.find( badge ) + 1
    return ( badge_priority )


while index < len( rucksack_contents ):
    group = rucksack_contents[ index: index+3: 1 ]    
    badge = find_badge( group )
    priority_sum += get_priority( badge )
    #print( str( start ) + " :: " + str(stop) + " :: " + badge + " :: " + priority[ priority.find( badge )  ] + " :: " + str( get_priority( badge ) ) + " :: " + str( group ) )
    index +=3

print( priority_sum )

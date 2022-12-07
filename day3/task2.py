import re

input = open('input.txt', 'r')

count = 0
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_sum = 0


def identify_compartments( contents ):
    content_length = int( len( contents ) )
    a_end = int( content_length / 2 )
    b_start = int( ( content_length / 2 ) )
    b_end = content_length
    a_contents = contents[ 0 : a_end ]
    b_contents = contents[ b_start : b_end : 1 ]

    return a_contents, b_contents

def identify_duplicate( a, b ):
    for char in a:
        if( b.find( char ) > -1 ):
            return char

def identify_group()

for line in input:
    a, b = identify_compartments( re.sub( '![a-zA-Z]','', line ) )
    duplicate = identify_duplicate( a, b )
    
    priority_sum += ( priority.find( duplicate ) + 1 )

input.close()

print( priority_sum )

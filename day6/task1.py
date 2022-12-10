with open("input.txt") as f:
    input = f.read().strip()
    f.close()

block_start = 0  #start index of 4-character block to check
block_end = 4    #end index of 4-character block to check

def has_duplicates( s ):
    has_duplicates = False

    for l in s:
        if s.count(l) > 1:
            has_duplicates = True
    
    return has_duplicates

while block_end < len(input):
    s = input[block_start:block_end]

    if( has_duplicates(s) == False ):
        print( block_end )
        break
    else:
        block_start +=1
        block_end +=1

input = open('input.txt', 'r')
total = 0 # Number of assignment pairs where 1 fully contains the other

def parse_assignments( line ):
    elf_assignments = line.split( ",", 1)
    elf1_start = int( elf_assignments[0].split( "-", 1 )[0] )
    elf1_end =  int( elf_assignments[0].split( "-", 1 )[1] )
    elf2_start = int ( elf_assignments[1].split( "-", 1 )[0] )
    elf2_end =  int ( elf_assignments[1].split( "-", 1 )[1] )

    return { "elf1_start": elf1_start, "elf1_end": elf1_end, "elf2_start": elf2_start, "elf2_end": elf2_end }

def check_contained( assignments ):
    if ( assignments["elf1_start"] >= assignments["elf2_start"] ) and ( assignments["elf1_end"] <= assignments["elf2_end"] ):
        return True
    elif ( assignments["elf2_start"] >= assignments["elf1_start"] ) and ( assignments["elf2_end"] <= assignments["elf1_end"] ):
        return True
    else:
        return False

for line in input:
    assignments = parse_assignments( line )

    fully_contained = check_contained( assignments )

    if( fully_contained):
        total +=1

print( str( total ))
import array
stacks = {
    "S1": array.array( "u", ["R","P","C","D","B","G"]),
    "S2": array.array( "u", ["H","V","G"]),
    "S3": array.array( "u", ["N","S","Q","D","J","P","M"]),
    "S4": array.array( "u", ["P","S","L","G","D","C","N","M"]),
    "S5": array.array( "u", ["J","B","N","C","P","F","L","S"]),
    "S6": array.array( "u", ["Q","B","D","Z","V","G","T","S"]),
    "S7": array.array( "u", ["B","Z","M","H","F","T","Q"]),
    "S8": array.array( "u", ["C","M","D","B","F"]),
    "S9": array.array( "u", ["F","C","Q","G"])
}

final_code = array.array("u",[])

with open("input.txt") as f:
    input = f.read().strip()
    f.close()

input = input.split("\n")

def parse_move_order( line ):    
    parts = line.split(" ")
    num_crates = int( parts[1] )
    origin = "S" + parts[3]
    destination = "S" + parts[5]
    
    return( {"num_crates": num_crates, "origin": origin, "destination": destination } )

def process_move_order( order ):
    for i in range(0, order[ "num_crates" ]):
        move_crate( order[ "origin" ], order["destination"])

def move_crate( origin, destination ):
    global stacks
    #print( "Moving 1 crate from stack " + origin + " to " + destination)
    stacks[ destination ].append( stacks[ origin ][ len( stacks[ origin ]) - 1] )
    stacks[ origin ].pop( len( stacks[ origin ] ) - 1 )

for line in input:
    if line.find("move") > -1:
        order = parse_move_order( line )
        process_move_order( order )

for stack in stacks:
    final_code.append( stacks[ stack ][ len(stacks[ stack ]) - 1 ] )

print( final_code )
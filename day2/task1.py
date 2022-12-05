input = open('input.txt', 'r')
score = 0
options = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}
choicePoints = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

resultPoints = {
    "LOSS": 0,
    "DRAW": 3,
    "WIN": 6
}

def decodeInput( code ):
    return options[ code ]

def calculate_result( them, us ):
    if( them == us):
        return "DRAW"
    elif( us == "SCISSORS" and them != "ROCK" ):
        return "WIN"
    elif( us == "ROCK" and them != "PAPER"):
        return "WIN"
    elif( us == "PAPER" and them != "SCISSORS"):
        return "WIN"
    else:
        return "LOSS"

def updateTotal( result, us ):
    global score
    score += resultPoints[ result ]
    score += choicePoints[ us ]

for line in input:
    
    them = decodeInput( line[0] )
    us = decodeInput( line[2] )
    result = calculate_result( them, us )
    updateTotal( result, us )

    #print( them + " :: " + us + " :: " + result + " :: " + str(score) )
    #break
input.close()

print( str(score) )

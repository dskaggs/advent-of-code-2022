input = open('input.txt', 'r')
score = 0
options = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "LOSS",
    "Y": "DRAW",
    "Z": "WIN"
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

def calculate_result( them, result ):
    if( result == "DRAW"):
        return them
    elif( result == "WIN" and them == "ROCK" ):
        return "PAPER"
    elif( result == "WIN" and them == "PAPER" ):
        return "SCISSORS"
    elif( result == "WIN" and them == "SCISSORS" ):
        return "ROCK"
    elif( result == "LOSS" and them == "ROCK" ):
        return "SCISSORS"
    elif( result == "LOSS" and them == "PAPER" ):
        return "ROCK"
    elif( result == "LOSS" and them == "SCISSORS" ):
        return "PAPER"

def updateTotal( result, us ):
    global score
    score += resultPoints[ result ]
    score += choicePoints[ us ]

for line in input:
    
    them = decodeInput( line[0] )
    result = decodeInput( line[2] )
    us = calculate_result( them, result )
    updateTotal( result, us )

    #print( them + " :: " + us + " :: " + result + " :: " + str(score) )
    #break
input.close()

print( str(score) )

import random

def roundDown(n, divisor):
    return n - (n % divisor)

def getBetMultiplier(n):
    if (n == 6 or n == 8):
        return 6
    else:
        return 5

def rollDice():
    DICE_MIN = 1
    DICE_MAX = 6
    dice1 = random.randint(DICE_MIN, DICE_MAX)
    dice2 = random.randint(DICE_MIN, DICE_MAX)
    return (dice1 + dice2)


def getPayout(diceOutcome, selectedNum, wager):
    if (diceOutcome == 7):
        return wager * -1

    elif (diceOutcome == selectedNum):
        if (selectedNum == 6 or selectedNum == 8):
            return (wager / 6) * 7

        elif (selectedNum == 5 or selectedNum == 9):
            return (wager / 5) * 7

        elif (selectedNum == 4 or selectedNum == 10):
            return (wager / 5) * 9
    else:
        return 0

def pressBet(b):
    return b * 2

def playGame(bets):
    gameBets = bets
    gameTotal = sum(bets.values()) * -1
    print('starting with {}'.format(gameTotal))

    r = 0
    while r != 7:
        r = rollDice() 
        if r == 7:
            print('seven out, loser')

        elif (r in gameBets.keys()):
            print('winner winner chicken dinner {}'.format(r))
            gameTotal += gameBets[r]
            #gameBets[r] = pressBet(gameBets[r])

        else:
            print('push nobody wins or loses {}'.format(r))

    return gameTotal



bankRoll = 1000
for i in range(1,10):
    selectedNums = {6: 10, 8:10}
    bankRoll += playGame(selectedNums)
    print(bankRoll)
print('final total {}'.format(bankRoll))

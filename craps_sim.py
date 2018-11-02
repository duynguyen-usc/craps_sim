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


def getPayout(diceOutcome, betAmount):
    if diceOutcome == 6 or diceOutcome == 8:
        return (betAmount / 6) * 7
    elif diceOutcome == 5 or diceOutcome == 9:
        return (betAmount / 5) * 7
    elif diceOutcome == 4 or diceOutcome == 10:
        return (betAmount / 5) * 9
    else:
        return 0


def pressBet(b):
    return b * 0.5

def playGame(bets):
    gameBets = bets
    startBetTotal = sum(bets.values())
    gameTotal = startBetTotal * -1
    print('starting with {}'.format(gameTotal))

    r = 0
    while r != 7: 
        print('roll bets: {}'.format(gameBets))
        r = rollDice() 
        if r == 7:
            print('seven out')

        elif (r in gameBets.keys()):
            payout = getPayout(r, gameBets[r])
            print('{0} winner winner chicken dinner {1}'.format(r, payout))

            gameTotal += payout
            if gameTotal >= gameBets[r]: 
                pressAmount = pressBet(gameBets[r])
                gameBets[r] = roundDown(gameBets[r] + pressAmount, getBetMultiplier(r))
                gameTotal = gameTotal - pressAmount
                print('pressed bet: {0}'.format(gameBets[r]))
        else:
            print('push nobody wins or loses {}'.format(r))

        print(gameTotal)
    return gameTotal


bankRoll = 1000

for i in range(1, 100):
    if bankRoll > 0:
        selectedNums = {4: 100, 6: 108, 8:108}
        bankRoll += playGame(selectedNums)
        print(bankRoll)


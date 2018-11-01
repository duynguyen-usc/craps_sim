import random
from types import SimpleNamespace

def rollDice():
	DICE_MIN = 1
	DICE_MAX = 6
	dice1 = random.randint(DICE_MIN,DICE_MAX)
	dice2 = random.randint(DICE_MIN,DICE_MAX)
	return (dice1 + dice2)

def getPayout(diceOutcome, selectedNum, wager):
	if (diceOutcome == 7):
		return wager * -1
	
	elif (diceOutcome == selectedNum):
		if(selectedNum == 6 or selectedNum == 8):
			return (wager / 6) * 7
		
		elif(selectedNum == 5 or selectedNum == 9):
			return (wager / 5) * 7
		
		elif(selectedNum == 4 or selectedNum == 10):
			return (wager / 5) * 9
	else:
		return 0
	

def playGame(selectedNum, startingBet):
	bet = roundDown(startingBet, getBetMultiplier(selectedNum))
	gamePL = 0
	rollResult = 0
	breakEven = 0
	while rollResult != 7:
		win = 0
		rollResult = rollDice()
		gamePL += getPayout(rollResult, selectedNum, bet)
		if(rollResult == selectedNum):
			if(breakEven >= startingBet):
				nextBet = bet * 1.5
				bet = roundDown(nextBet, getBetMultiplier(selectedNum))
			else:
				breakEven += gamePL
				gamePL = 0
	return (gamePL + breakEven)

def roundDown(n, divisor):
	return n - (n % divisor)

def getBetMultiplier(n):
	if (n == 6 or n == 8):
		return 6
	else: 
		return 5

bankRoll = 1000
startBet = 100
tries = 100
for i in range(1, tries):
	if (bankRoll >= startBet):
		pL = playGame(4, startBet)
		print("game: {}".format(pL))
		bankRoll = bankRoll + pL
print("final bankroll: {}".format(bankRoll))
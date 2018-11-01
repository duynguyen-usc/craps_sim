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
		if(selectedNum == 6 or num == 8):
			return (wager / 6) * 7
		
		elif(selectedNum == 5 or selectedNum == 9):
			return (wager / 5) * 7
		
		elif(selectedNum == 4 or selectedNum == 10):
			return (wager / 5) * 9
	else:
		return 0
	

def playGame(selectedNum, startingBet):
	bet = startingBet
	gamePL = 0
	rollResult = 0
	while rollResult != 7:
		win = 0
		print(bet)
		rollResult = rollDice()
		gamePL = getPayout(rollResult, selectedNum, bet)
		if(rollResult == selectedNum):
			print('winner!')
			bet = roundDown(bet * 1.5, 6)
		elif(rollResult ==7):
			print('loser!')
	return gamePL

def roundDown(n, divisor):
	return n - (n % divisor)




bankRoll = 1000
for i in range(1, 10):
	pL = playGame(6, 108)
	print("game={}".format(pL))
	bankRoll = bankRoll + pL

print("final bankroll = {}".format(bankRoll))
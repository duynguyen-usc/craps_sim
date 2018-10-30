import random

def rollDice(num, wager):
	DICE_MIN = 1
	DICE_MAX = 6
	dice1 = random.randint(DICE_MIN,DICE_MAX)
	dice2 = random.randint(DICE_MIN,DICE_MAX)
	dsum = dice1 + dice2
	
	payout = 0
	if (dsum == 7):
		payout = wager * -1

	elif (num == dsum):
		if(num == 6 or num == 8):
			payout = (wager / 6) * 7
		
		elif(num == 5 or num == 9):
			payout = (wager / 5) * 7
		
		elif(num == 5 or num == 9):
			payout = (wager / 5) * 9
	else:
		payout = 0
	return {'result': dsum, 'payout': payout}

# inputs
bankRoll = 10000
selectedNum = 6
wager = 108

for x in range(1, 100):
	betOutcome = rollDice(selectedNum, wager)
	bankRoll = bankRoll + betOutcome['payout']

print(bankRoll)

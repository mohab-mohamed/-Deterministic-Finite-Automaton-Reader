#!/usr/bin/env

def main():
	try:
		stateInput = input()
		stateLine = stateInput.split(' ')
		lengthOfStateLine = len(stateLine)
		states = []
		for x in range(1, (lengthOfStateLine)):
			states.append(stateLine[x])
#		print(states)
		
		symbolInput = input()
		symbolLine = symbolInput.split(' ')
		lengthOfSymbolLine = len(symbolLine)
		symbols = []
		for x in range(1, (lengthOfSymbolLine)):
			symbols.append(symbolLine[x])
#		print(symbols)
		
		beginRules = input()
		rules = []
		booleanValue = True
		end = 'end_rules'
		while (booleanValue == True):
			ruleInput = input()
			if(ruleInput == end):
				booleanValue = False
				break
			rules.append(ruleInput.split(' ')[4])
			rules.append(ruleInput.split(' ')[0])
			rules.append(ruleInput.split(' ')[2])

		lengthOfRules = len(rules)
		startLine = input()
		start = startLine.split(' ')[1]
		finalInput = input()
		finalLine = finalInput.split(' ')
		final = []
		lengthOfFinalLine = len(finalLine)
		for x in range(1, lengthOfFinalLine):
			final.append(finalLine[x])
		lengthOfFinal = len(final)
#		print(final)
#		print(start)
		while True:
			pathInput = input()
			path = list(pathInput)
			lengthOfPath = len(path)
#			print(path)
			currentState = start
			endReached = False
			rulesBroke = False
			for x in range(0, lengthOfPath):
				currentLetter = path[x]
				endReached = False
				rulesBroke = False
				for y in range(0, lengthOfRules, 3):
					rulesBroke = False
					if(endReached == True):
						break	
					if(currentLetter != rules[y]):
						continue
					if(currentLetter == rules[y]):
						if((currentState == rules[y+1])):
							currentState = rules[y+2]
							for z in range(lengthOfFinal):
								if(currentState == final[z]):
									endReached = True
						elif(currentState == rules[y+2]):
							continue
						else:
							rulesBroke = True
							continue
#			print(rules)
#			print(endReached)
#			print(rulesBroke)
			if ((endReached == True) and (rulesBroke == False)):
				print('accepted')
			else:
				print('rejected')
	except EOFError:
		exit()

if __name__ == '__main__':
	main()

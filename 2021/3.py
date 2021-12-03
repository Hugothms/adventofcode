import sys
userInput = sys.stdin.readlines()

values = []
for word in userInput:
	word = word.strip()
	values.append(word)

gamma = ''
epsilon = ''
for i in range(len(values[0])):
	cpt = 0
	for value in values:
		if value[i] == '1':
			cpt += 1
	if cpt > len(values)/2:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

print(int(gamma, base=2) * int(epsilon, base=2))	# 2640986
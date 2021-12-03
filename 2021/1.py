import sys
userInput = sys.stdin.readlines()

values = []
for word in userInput:
	word = word.strip()
	values.append(int(word))

cpt = 0
for i in range(len(values) - 3):
	first = values[i] + values[i+1] + values[i+2]
	second = values[i+3] + values[i+1] + values[i+2]
	if second > first:
		cpt += 1

print(cpt)	# 1359
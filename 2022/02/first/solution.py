with open('../input') as f:
    file = f.readlines()
    # print(lines)

lines = []
for line in file:
    lines.append(line.replace("\n", ""))


form_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

combinason = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}


round_score = 0
for line in lines:
    round_score += (combinason[line])
    round_score += (form_score[line[2]])
print(round_score)

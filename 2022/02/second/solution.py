with open('../input') as f:
    file = f.readlines()
    # print(lines)

lines = []
for line in file:
    lines.append(line.replace("\n", ""))


form_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

combinason = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1,
}


round_score = 0
for line in lines:
    round_score += (combinason[line])
    round_score += (form_score[line[2]])
print(round_score)

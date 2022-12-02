with open('../input') as f:
    file = f.readlines()
    # print(lines)

lines = []
for line in file:
    lines.append(line.replace("\n", ""))

output = []
sum = 0
for line in lines:
    if (len(line) == 0):
        output.append(sum)
        sum = 0
        # print("empty")
    else:
        sum += int(line)
        # print(line)

max = 0
for value in output:
    if (max < value):
        max = value

print(max)

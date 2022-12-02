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

max_values = []
max_values.append(output.pop(output.index(max(output))))
max_values.append(output.pop(output.index(max(output))))
max_values.append(output.pop(output.index(max(output))))

print(max_values)
print(max_values[2]+max_values[1]+max_values[0])

import numpy as np

instructions = np.loadtxt('days/day_01/input.txt', dtype=str).item()

floor = 0
basement = 0
for i, instruction in enumerate(instructions):
    match instruction:
        case '(':
            floor += 1
        case ')':
            floor -= 1
    if basement <= 0 and floor < 0:
        basement = i + 1


print(floor)
print(basement)
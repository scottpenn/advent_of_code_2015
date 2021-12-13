
from collections import Counter
import numpy as np


directions = np.loadtxt('days/day_03/input.txt', dtype=str).item()

current_position = (0, 0)
houses = Counter([current_position, current_position])

for direction in directions:
    x, y = current_position
    match direction:
        case '^':
            current_position = (x, y + 1)
        case 'v':
            current_position = (x, y - 1)
        case '>':
            current_position = (x + 1, y)
        case '<':
            current_position = (x - 1, y)
    houses[current_position] += 1

print(len(houses))

santa_position = (0, 0)
robo_position = (0, 0)
houses = Counter([santa_position, robo_position])

for direction in directions[0::2]:
    x, y = santa_position
    match direction:
        case '^':
            santa_position = (x, y + 1)
        case 'v':
            santa_position = (x, y - 1)
        case '>':
            santa_position = (x + 1, y)
        case '<':
            santa_position = (x - 1, y)
    houses[santa_position] += 1

for direction in directions[1::2]:
    x, y = robo_position
    match direction:
        case '^':
            robo_position = (x, y + 1)
        case 'v':
            robo_position = (x, y - 1)
        case '>':
            robo_position = (x + 1, y)
        case '<':
            robo_position = (x - 1, y)
    houses[robo_position] += 1

print(len(houses))
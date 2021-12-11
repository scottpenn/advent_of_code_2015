import numpy as np
import timeit

instructions = np.loadtxt('days/day_1/input.txt', dtype=str).item()

# Begin
start = timeit.default_timer()

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

# End
stop = timeit.default_timer()

print('Time: ', stop - start)
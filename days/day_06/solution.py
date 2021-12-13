import numpy as np

regex = r'(\D*)\s(\d*),(\d*) through (\d*),(\d*)\n*'
instructions = np.fromregex('days/day_06/input.txt', regex,
    [('how', 'O'), ('x1', 'i'), ('y1', 'i'), ('x2', 'i'), ('y2', 'i')])

lights_part_1 = np.zeros((1000, 1000))
lights_part_2 = np.zeros((1000, 1000), dtype=int)

for instruction in instructions:
    x1, y1 = instruction['x1'], instruction['y1']
    x2, y2 = instruction['x2'] + 1, instruction['y2'] + 1
    if instruction['how'] == 'turn on':
        lights_part_1[x1:x2, y1:y2] = 1
        lights_part_2[x1:x2, y1:y2] += 1
    elif instruction['how'] == 'turn off':
        lights_part_1[x1:x2, y1:y2] = 0
        lights_part_2[x1:x2, y1:y2] -= 1
        lights_part_2 = np.where(lights_part_2 < 0, 0, lights_part_2)
    else:
        lights_part_1[x1:x2, y1:y2] = np.where(lights_part_1[x1:x2, y1:y2] == 1, 0, 1)
        lights_part_2[x1:x2, y1:y2] += 2
    
print(np.count_nonzero(lights_part_1))
print(np.sum(lights_part_2))
import numpy as np

presents = np.loadtxt('days/day_02/input.txt', delimiter='x', dtype=int)

length = presents[:, 0]
width = presents[:, 1]
height = presents[:, 2]

lw = length * width
wh = width * height
hl = height * length
slack = np.min([lw, wh, hl], axis=0)

paper_needed = 2 * lw + 2 * wh + 2 * hl + slack

print(np.sum(paper_needed))

longest_side = np.max([length, width, height], axis=0)

shortest_perimeter = 2 * length + 2 * width + 2 * height - 2 * longest_side

cubic_volume = length * width * height

ribbon_needed = shortest_perimeter + cubic_volume

print(np.sum(ribbon_needed))
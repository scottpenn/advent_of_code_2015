import numpy as np

literals = np.loadtxt('days/day_08/input.txt', delimiter='\n', dtype=str)

print(sum(len(literal) - eval(f'len({literal})') for literal in literals))

print(sum(2 + np.count_nonzero([c in ['\\', '"'] for c in literal]) for literal in literals))

import numpy as np
import hashlib

partial_key = np.loadtxt('days/day_04/input.txt', dtype=str).item()

i = 1
found_five = False
while True:
    secret_key = f'{partial_key}{i}'
    md5_hash = hashlib.md5(secret_key.encode()).hexdigest()
    if not found_five and md5_hash[:5] == '00000':
        found_five = True
        print(i)
    if found_five and md5_hash[:6] == '000000':
        print(i)
        break
    i += 1

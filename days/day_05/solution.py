import numpy as np

strings = np.loadtxt('days/day_05/input.txt', dtype=str)


vowels = ['a', 'e', 'i', 'o', 'u']
forbidden_strings = ['ab', 'cd', 'pq', 'xy']
nice_string_count = 0
for string in strings:
    nice = True
    vowel_count = 0
    last_letter = ''
    double_letter_count = 0
    for letter in string:
        if letter in vowels:
            vowel_count += 1
        if (last_letter + letter) in forbidden_strings:
            nice = False
            break
        if last_letter == letter:
            double_letter_count += 1
        last_letter = letter
    if vowel_count < 3:
        nice = False
    if double_letter_count < 1:
        nice = False
    if nice:
        nice_string_count += 1

print(nice_string_count)
        
nice_string_count = 0
for string in strings:
    nice = False
    for i in range(len(string) - 1):
        pair = string[i:i+2]
        if pair in string[:i] or pair in string[i+2:]:
            nice = True
    if not nice:
        continue
    nice = False
    for i in range(len(string) - 2):
        trio = string[i:i+3]
        if trio[0] == trio[2]:
            nice = True
    if nice:
        nice_string_count += 1

print(nice_string_count)
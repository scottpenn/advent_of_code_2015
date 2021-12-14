import numpy as np
import re

instructions = np.loadtxt('days/day_07/input.txt', delimiter='\n', dtype=str)

def resolve_wires(instructions, override=False, override_value=0):
    wires = {}
    while len(instructions) > 0:
        unresolved_instructions = []
        for instruction in instructions:
            if (match := re.match('(\d*) -> (\w*)', instruction)):
                signal, wire = match.groups()
                if wire == 'b' and override:
                    wires[wire] = override_value
                else:
                    wires[wire] = int(signal)
            elif (match := re.match('([a-z]*) -> (\w*)', instruction)):
                signal_wire, wire = match.groups()
                if signal_wire in wires:
                    wires[wire] = wires[signal_wire]
                else:
                    unresolved_instructions.append(instruction)
            elif (match := re.match('([a-z]*) AND ([a-z]*) -> (\w*)', instruction)):
                a, b, c = match.groups()
                if a in wires and b in wires:
                    wires[c] = wires[a] & wires[b]
                else:
                    unresolved_instructions.append(instruction)
            elif (match := re.match('(\d*) AND ([a-z]*) -> (\w*)', instruction)):
                a, b, c = match.groups()
                if b in wires:
                    wires[c] = int(a) & wires[b]
                else:
                    unresolved_instructions.append(instruction)
            elif (match := re.match('(\w*) OR (\w*) -> (\w*)', instruction)):
                a, b, c = match.groups()
                if a in wires and b in wires:
                    wires[c] = wires[a] | wires[b]
                else:
                    unresolved_instructions.append(instruction)
            elif (match := re.match('NOT (\w*) -> (\w*)', instruction)):
                a, b = match.groups()
                if a in wires:
                    wires[b] = ~wires[a]
                else:
                    unresolved_instructions.append(instruction)
            elif (match := re.match('(\w*) LSHIFT (\d*) -> (\w*)', instruction)):
                a, b, c = match.groups()
                if a in wires:
                    wires[c] = wires[a] << int(b)
                else:
                    unresolved_instructions.append(instruction)
            elif (match := re.match('(\w*) RSHIFT (\d*) -> (\w*)', instruction)):  
                a, b, c = match.groups()  
                if a in wires:
                    wires[c] = wires[a] >> int(b)
                else:
                    unresolved_instructions.append(instruction)
            else:
                print("unmatched instruction")
                print(instruction)
        if 'a' in wires:
            break
        instructions = unresolved_instructions
    return wires['a']

override = resolve_wires(instructions)

print(override)

print(resolve_wires(instructions, override=True, override_value=override))
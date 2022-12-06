import re

def part1(lines):
    cargo_ship = [[] for i in range(9)]
    for line in lines:
        if 'move' not in line:
            if '[' in line and ']' in line:
                line = line.replace('\n', '')
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace('  ', ' ')
                new_line = [line[i] for i in range(0, len(line), 2)]
                for i, ch in enumerate(new_line):
                    if ch != ' ':
                        cargo_ship[i].append(ch)
        elif 'move' in line:
            line = line.replace('\n', '')
            numbers = re.findall("\d+", line)
            numbers = [int(x) for x in numbers]
            for i in range(numbers[0]):
                element = cargo_ship[numbers[1]-1].pop(0)
                cargo_ship[numbers[2]-1].insert(0, element)
    
    top = [x[0] for x in cargo_ship]
    return top

def part2(lines):
    cargo_ship = [[] for i in range(9)]
    for line in lines:
        if 'move' not in line:
            if '[' in line and ']' in line:
                line = line.replace('\n', '')
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace('  ', ' ')
                new_line = [line[i] for i in range(0, len(line), 2)]
                for i, ch in enumerate(new_line):
                    if ch != ' ':
                        cargo_ship[i].append(ch)
        elif 'move' in line:
            line = line.replace('\n', '')
            numbers = re.findall("\d+", line)
            numbers = [int(x) for x in numbers]
            for i in range(numbers[0]):
                element = cargo_ship[numbers[1]-1].pop(0)
                cargo_ship[numbers[2]-1].insert(i, element)
    
    top = [x[0] for x in cargo_ship]
    return top

with open('input.txt', 'r') as f:
    lines = f.readlines()
    top = part1(lines)
    top2 = part2(lines)

top = ''.join(top)
top2 = ''.join(top2)

print(f'The top is {top}')
print(f'The top of part two is {top2}')

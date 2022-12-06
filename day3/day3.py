def part1(lines, case_values):
    total_value = 0
    for line in lines:
        line = line.strip()
        mid = len(line) // 2
        first_comp = line[:mid]
        second_comp = line[mid:]
        intersect = set(first_comp).intersection(second_comp)
        repeated = next(iter(intersect))
        total_value += case_values[repeated]

    return total_value

def part2(lines, case_values):
    total_value = 0
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        group = [set(group[j].strip()) for j in range(3)]
        intersection = group[0] & group[1] & group[2]
        badge = next(iter(intersection))
        total_value += case_values[badge]

    return total_value

case_values = {}
count_value = 1
for i in range(97, 123):
    case_values[chr(i)] = count_value
    count_value += 1

for i in range(65, 91):  
    case_values[chr(i)] = count_value
    count_value += 1

total_value = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    total_value = part1(lines, case_values)
    total_value_2 = part2(lines, case_values)
    
print(f'Total value repeated rucksack {total_value}')
print(f'Total value badge rucksack {total_value_2}')

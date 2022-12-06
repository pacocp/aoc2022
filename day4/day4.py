def part1(lines):
    total_contained = 0
    for line in lines:
        line = line.strip().split(',')
        first = line[0].split('-')
        second = line[1].split('-')
        range1 = list(range(int(first[0]), int(first[1])+1))
        range2 = list(range(int(second[0]), int(second[1])+1))

        if set(range2).issubset(set(range1)) or set(range1).issubset(range2):
            total_contained += 1

    return total_contained

def part2(lines):
    total_repeated = 0
    for line in lines:
        line = line.strip().split(',')
        first = line[0].split('-')
        second = line[1].split('-')
        range1 = list(range(int(first[0]), int(first[1])+1))
        range2 = list(range(int(second[0]), int(second[1])+1))
        
        intersect = set(range1) & set(range2)

        if intersect:
            total_repeated += 1

    return total_repeated

with open('input.txt', 'r') as f:
    lines = f.readlines()
    total_contained = part1(lines)
    total_repeated = part2(lines)

print(f'Sections totally contained {total_contained}')
print(f'Sections with at least one element {total_repeated}')

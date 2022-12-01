with open('input.txt', 'r') as f:
    calories_elfs = []
    count_cal = 0
    for line in f.readlines():
        if line != '\n':
            count_cal += int(line.replace('\n', ''))
        elif line == '\n':
            calories_elfs.append(count_cal)
            count_cal = 0

print(f'Maximum number of calories carried {max(calories_elfs)}')
print(f'Top three number of calories carried {sum(sorted(calories_elfs)[-3:])}')



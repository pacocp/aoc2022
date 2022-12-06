def part1(message):
    characters = 4
    for i in range(len(message)):
        marker = set(message[i:i+4])
        if len(marker) == 4:
            return characters
        else:
            characters += 1
    return characters
    
def part2(message):
    characters = 14
    for i in range(len(message)):
        marker = set(message[i:i+14])
        if len(marker) == 14:
            return characters
        else:
            characters += 1
    return characters
    
with open('input.txt', 'r') as f:
    lines = f.readlines()
    message = lines[0]
    start_marker = part1(message)
    message_marker = part2(message)

print(f'Number of characters until first start-of-packet {start_marker}')
print(f'Number of characters until first start-of-message {message_marker}')

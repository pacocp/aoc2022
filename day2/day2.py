def total_score_first(lines):
    list_wins = ['A Y', 'B Z', 'C X']
    list_draws = ['A X', 'B Y', 'C Z']
    scores_my_choice = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    total_score = 0
    for line in lines:
        play = line.replace('\n', '')
        if play in list_wins:
            total_score += 6
        elif play in list_draws:
            total_score += 3
        
        total_score += scores_my_choice[play.split(' ')[-1]]
    
    return total_score

def total_score_second(lines):
    scores = {'X': 0, 'Y': 3, 'Z': 6}
    scores_selection = {'A Y': 1, 'A Z': 2, 'A X': 3, 'B Y': 2, 'B Z': 3, 'B X': 1, 'C Y': 3, 'C Z': 1, 'C X': 2}
    total_score = 0
    for line in lines:
        play = line.replace('\n', '')
        total_score += scores[play.split(' ')[-1]]
        total_score += scores_selection[play]

    return total_score

with open('input.txt', 'r') as f:
    lines = f.readlines()
    total_score = total_score_first(lines)
    total_score_2 = total_score_second(lines)
print(f'Total score obtained first part {total_score}')
print(f'Total score obtained second part {total_score_2}')


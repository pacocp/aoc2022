import numpy as np
def read_matrix(lines):
    matrix = []
    for line in lines:
        line = line.strip()
        matrix.append([*line])

    return np.array(matrix)

def part1(matrix):
    h, w = matrix.shape
    visible = h * 2 + (w*2) - 4
    for r in range(1, h-1):
        for c in range(1, w-1):
            tree_height = matrix[r, c]
            row = matrix[r, :]
            col = matrix[:, c]
            if all(row[:c] < tree_height) or \
                    all(row[c+1:] < tree_height) or \
                    all(col[:r] < tree_height) or \
                    all(col[r+1:] < tree_height):
                visible += 1

    return visible

def part2(matrix):
    def score_line(indexes, line, tree_height):
        score = 0
        for j in indexes:
            score += 1
            if line[j] >= tree_height:
                break

        return score

    h, w = matrix.shape
    scores = []
    for r in range(1, h-1):
        for c in range(1, w-1):
            tree_height = matrix[r, c]
            row = matrix[r, :]
            col = matrix[:, c]
            left = score_line(range(c-1, -1, -1), row, tree_height)
            right = score_line(range(c+1, len(row)), row, tree_height)
            top = score_line(range(r-1, -1, -1), col, tree_height)
            botton = score_line(range(r+1, len(col)), col, tree_height)
            scores.append(left*right*top*botton)

    return max(scores)

if __name__ == '__main__':
    TESTDATA = [
            [3,0,3,7,3],
            [2,5,5,1,2],
            [6,5,3,3,2],
            [3,3,5,4,9],
            [3,5,3,9,0]]
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    matrix = read_matrix(lines)
    visible = part1(matrix)
    max_score = part2(matrix)
    print(f'Number of visible trees {visible}')
    print(f'Maximum score {max_score}')

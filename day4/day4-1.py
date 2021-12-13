#%%
import numpy
inputfile = open('./day4-input.txt')
lines = inputfile.readlines()
bingo_nums = lines[0].split(',')
bingo_nums = [int(i) for i in bingo_nums]
bingo_cards = [[int(n) for n in i.split()] for i in lines[2:] if i != '\n']
num_boards = len(bingo_cards) // 5
cards = numpy.array(bingo_cards).reshape((num_boards,5,5))
# %%
marked_boards = numpy.zeros((num_boards,5,5), dtype=int)
winning_boards = []
scores = []

def mark_board(n):
    for z in range(num_boards):
        if z in winning_boards:
            continue
        for y in range(5):
            for x in range(5):
                if cards[z,x,y] == n:
                    marked_boards[z,x,y] = 1

def check_win():
    for index in range(num_boards):
        if index in winning_boards:
            continue
        for i in range(5):
            if sum(marked_boards[index, i, 0:]) == 5:
                winning_boards.append(index)
                scores.append(get_board_score(index))
                continue #no need to check Y if X is a winner
            if sum(marked_boards[index, 0:, i]) == 5:
                winning_boards.append(index)
                scores.append(get_board_score(index))

def get_board_score(winning_board_index):
    unmarked = []
    for x in range(5):
        for y in range(5):
            if not marked_boards[winning_board_index, x, y]:
                unmarked.append(cards[winning_board_index,x,y])
    return sum(unmarked) * number


# %%

for number in bingo_nums:
    mark_board(number)
    check_win()

# %%
scores[0]
scores[-1]
# %%

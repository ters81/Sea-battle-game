
from random import choice, randint

# 0 - empty cell
# 1 - cell with a ship
# 8 - forbidden cell (no other ship can stand here)


# Create empty field
field = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
        ]


def choice_of_direction():
    # Random choice of ship direction (horizontal or vertical)
    return choice(['horizontal', 'vertical'])

# Adding a four-deck ship
direction =  choice_of_direction()

if direction == 'horizontal':
    starting_cell_row = randint(1, 10)

    starting_cell_column = randint(1, 7)
    scc = starting_cell_column

    print(starting_cell_row, starting_cell_column)

    for _ in range(4):
        field[starting_cell_row][scc] = 1
        scc += 1

    for row in [starting_cell_row - 1, starting_cell_row + 1]:
        scc = starting_cell_column - 1
        for _ in range(6):
            field[row][scc] = 8
            scc += 1

    field[starting_cell_row][starting_cell_column - 1] = 8
    field[starting_cell_row][starting_cell_column + 4] = 8


else:
    starting_cell_row = randint(1, 7)
    scr = starting_cell_row

    starting_cell_column = randint(1, 10)

    print(starting_cell_row, starting_cell_column)

    for i in range(4):
        field[starting_cell_row][starting_cell_column] = 1
        starting_cell_row += 1


for i in range(12):
    print(field[i])

print(direction)



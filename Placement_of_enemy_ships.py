
from random import choice, randint

# 0 - empty cell
# 1 - cell with a ship
# 8 - forbidden cell (no other ship can stand here)


# Create empty field
field = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]


def choice_of_direction():
    # Random choice of ship direction (horizontal or vertical)
    return choice(['horizontal', 'vertical'])

# Adding a four-deck ship
direction =  choice_of_direction()

if direction == 'horizontal':
    starting_cell_row = randint(0, 9)
    starting_cell_column = randint(0, 6)
    print(starting_cell_row, starting_cell_column)
    for i in range(4):
        field[starting_cell_row][starting_cell_column] = 1
        starting_cell_column += 1
    if starting_cell_row > 0:
        starting_cell_row -= 1
        starting_cell_column -= 5
        for i in range(6):
            field[starting_cell_row][starting_cell_column] = 8
            starting_cell_column += 1

else:
    starting_cell_row = randint(0, 6)
    starting_cell_column = randint(0, 9)
    print(starting_cell_row, starting_cell_column)
    for i in range(4):
        field[starting_cell_row][starting_cell_column] = 1
        starting_cell_row += 1


for i in range(10):
    print(field[i])

print(direction)



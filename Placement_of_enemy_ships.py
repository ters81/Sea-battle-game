
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
list_of_empty_cells = [
    '1-1', '1-2', '1-3', '1-4', '1-5', '1-6', '1-7', '1-8', '1-9', '1-10',
    '2-1', '2-2', '2-3', '2-4', '2-5', '2-6', '2-7', '2-8', '2-9', '2-10',
    '3-1', '3-2', '3-3', '3-4', '3-5', '3-6', '3-7', '3-8', '3-9', '3-10',
    '4-1', '4-2', '4-3', '4-4', '4-5', '4-6', '4-7', '4-8', '4-9', '4-10',
    '5-1', '5-2', '5-3', '5-4', '5-5', '5-6', '5-7', '5-8', '5-9', '5-10',
    '6-1', '6-2', '6-3', '6-4', '6-5', '6-6', '6-7', '6-8', '6-9', '6-10',
    '7-1', '7-2', '7-3', '7-4', '7-5', '7-6', '7-7', '7-8', '7-9', '7-10',
    '8-1', '8-2', '8-3', '8-4', '8-5', '8-6', '8-7', '8-8', '8-9', '8-10',
    '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7', '9-8', '9-9', '9-10',
    '10-1', '10-2', '10-3', '10-4', '10-5', '10-6', '10-7', '10-8', '10-9', '10-10'
]

# Adding a four-deck ship

direction = choice(['horizontal', 'vertical'])
starting_cell = choice(list_of_empty_cells).split('-')

# starting_cell = '5-1'  # Проверка

starting_cell_row = int(starting_cell[0])
starting_cell_column = int(starting_cell[1])

print(starting_cell_row, starting_cell_column)

if direction == 'horizontal':
    # If the initial position of the ship will cause it to go out of the field.
    if starting_cell_column == 8:
        starting_cell_column -= randint(1, 7)
    elif starting_cell_column == 9:
        starting_cell_column -= randint(2, 8)
    elif starting_cell_column == 10:
        starting_cell_column -= randint(3, 9)

    scc = starting_cell_column

    # remove used cells from the list
    for _ in range(4):
        field[starting_cell_row][scc] = 1
        list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))
        scc += 1
    if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells :
        list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

    scc = starting_cell_column - 1
    if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells :
        list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

    field[starting_cell_row][starting_cell_column - 1] = 8
    field[starting_cell_row][starting_cell_column + 4] = 8

    # removal of used cells from the list if the ship is adjacent to the borders of the field
    if 1 < starting_cell_row < 10:
        for row in [starting_cell_row - 1, starting_cell_row + 1]:
            scc = starting_cell_column - 1
            for _ in range(6):
                field[row][scc] = 8
                if (str(row) + '-' + str(scc)) in list_of_empty_cells:
                    list_of_empty_cells.remove(str(row) + '-' + str(scc))
                scc += 1
    elif starting_cell_row == 1:
        scc = starting_cell_column - 1
        for _ in range(6):
            field[starting_cell_row + 1][scc] = 8
            if (str(starting_cell_row + 1) + '-' + str(scc)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(starting_cell_row + 1) + '-' + str(scc))
            scc += 1
    elif starting_cell_row == 10:
        scc = starting_cell_column - 1
        for _ in range(6):
            field[starting_cell_row - 1][scc] = 8
            if (str(starting_cell_row - 1) + '-' + str(scc)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(starting_cell_row - 1) + '-' + str(scc))
            scc += 1

else:
    # If the initial position of the ship will cause it to go out of the field.
    if starting_cell_row == 8:
        starting_cell_row -= randint(1, 7)
    elif starting_cell_row == 9:
        starting_cell_row -= randint(2, 8)
    elif starting_cell_row == 10:
        starting_cell_row -= randint(3, 9)

    scr = starting_cell_row

    # remove used cells from the list
    for _ in range(4):
        field[scr][starting_cell_column] = 1
        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))
        scr += 1
    if (str(scr) + '-' + str(starting_cell_column)) in list_of_empty_cells:
        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))

    scr = starting_cell_row - 1
    if (str(scr) + '-' + str(starting_cell_column)) in list_of_empty_cells :
        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))

    field[starting_cell_row-1][starting_cell_column] = 8
    field[starting_cell_row+4][starting_cell_column] = 8

    # removal of used cells from the list if the ship is adjacent to the borders of the field
    if 1 < starting_cell_column < 10:
        for column in [starting_cell_column - 1, starting_cell_column + 1]:
            scr = starting_cell_row - 1
            for _ in range(6):
                field[scr][column] = 8
                if (str(scr) + '-' + str(column)) in list_of_empty_cells:
                    list_of_empty_cells.remove(str(scr) + '-' + str(column))
                scr += 1
    elif starting_cell_column == 1:
        scr = starting_cell_row - 1
        for _ in range(6):
            field[scr][starting_cell_column + 1] = 8
            if (str(scr) + '-' + str(starting_cell_column + 1)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column + 1))
            scr += 1
    elif starting_cell_column == 10:
        scr = starting_cell_row - 1
        for _ in range(6):
            field[scr][starting_cell_column - 1] = 8
            if (str(scr) + '-' + str(starting_cell_column - 1)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column - 1))
            scr += 1


for i in range(12):
    print(field[i])

print(direction)

print(list_of_empty_cells)
print(len(list_of_empty_cells))
from random import choice, randint
from Position_of_a_ship_with_2_slots import Position_of_a_ship_with_2_slots

# 0 - empty cell
# 1 - cell with a ship
# 8 - forbidden cell (no other ship can stand here)

field, list_of_empty_cells = Position_of_a_ship_with_2_slots()

# for i in range(12):
#     print(field[i])

count_of_ship_1 = 0

# Adding a 2-deck ship
def Position_of_a_ship_with_1_slots():

    def Ship_1_call():

        global count_of_ship_1
        count_of_ship_1 += 1

        scc = starting_cell_column
        # remove used cells from the list

        field[starting_cell_row][scc] = 1
        list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

        scc += 1
        if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells:
            list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

        scc = starting_cell_column - 1
        if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells:
            list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

        field[starting_cell_row][starting_cell_column - 1] = 8
        field[starting_cell_row][starting_cell_column + 1] = 8
        # removal of used cells from the list if the ship is adjacent to the borders of the field
        if 1 < starting_cell_row < 10:
            for row in [starting_cell_row - 1, starting_cell_row + 1]:
                scc = starting_cell_column - 1
                for _ in range(3):
                    field[row][scc] = 8
                    if (str(row) + '-' + str(scc)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(row) + '-' + str(scc))
                    scc += 1
        elif starting_cell_row == 1:
            scc = starting_cell_column - 1
            for _ in range(3):
                field[starting_cell_row + 1][scc] = 8
                if (str(starting_cell_row + 1) + '-' + str(scc)) in list_of_empty_cells:
                    list_of_empty_cells.remove(str(starting_cell_row + 1) + '-' + str(scc))
                scc += 1
        elif starting_cell_row == 10:
            scc = starting_cell_column - 1
            for _ in range(3):
                field[starting_cell_row - 1][scc] = 8
                if (str(starting_cell_row - 1) + '-' + str(scc)) in list_of_empty_cells:
                    list_of_empty_cells.remove(str(starting_cell_row - 1) + '-' + str(scc))
                scc += 1

    # ==============================================================================================================

    while count_of_ship_1 < 4:

        starting_cell = choice(list_of_empty_cells).split('-')

        starting_cell_row = int(starting_cell[0])
        starting_cell_column = int(starting_cell[1])

        # print(starting_cell_row, starting_cell_column, direction)

        Ship_1_call()

    return field, list_of_empty_cells


Position_of_a_ship_with_1_slots()

for i in range(12):
    print(field[i])

print(list_of_empty_cells)
print(len(list_of_empty_cells))

print('количество кораблей_1 -', count_of_ship_1, 'шт.')

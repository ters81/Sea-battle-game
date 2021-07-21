from random import choice, randint
from Position_of_a_ship_with_3_slots import Position_of_a_ship_with_3_slots

# 0 - empty cell
# 1 - cell with a ship
# 8 - forbidden cell (no other ship can stand here)

field, list_of_empty_cells = Position_of_a_ship_with_3_slots()

# for i in range(12):
#     print(field[i])

count_of_ship_2 = 0

# Adding a 2-deck ship
def Position_of_a_ship_with_2_slots():

    def Ship_2_call():

        global count_of_ship_2
        count_of_ship_2 += 1

        if direction == 'horizontal':
            scc = starting_cell_column
            # remove used cells from the list
            for _ in range(2):
                field[starting_cell_row][scc] = 1
                list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))
                scc += 1
            if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

            scc = starting_cell_column - 1
            if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

            field[starting_cell_row][starting_cell_column - 1] = 8
            field[starting_cell_row][starting_cell_column + 2] = 8

            # removal of used cells from the list if the ship is adjacent to the borders of the field
            if 1 < starting_cell_row < 10:
                for row in [starting_cell_row - 1, starting_cell_row + 1]:
                    scc = starting_cell_column - 1
                    for _ in range(4):
                        field[row][scc] = 8
                        if (str(row) + '-' + str(scc)) in list_of_empty_cells:
                            list_of_empty_cells.remove(str(row) + '-' + str(scc))
                        scc += 1
            elif starting_cell_row == 1:
                scc = starting_cell_column - 1
                for _ in range(4):
                    field[starting_cell_row + 1][scc] = 8
                    if (str(starting_cell_row + 1) + '-' + str(scc)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(starting_cell_row + 1) + '-' + str(scc))
                    scc += 1
            elif starting_cell_row == 10:
                scc = starting_cell_column - 1
                for _ in range(4):
                    field[starting_cell_row - 1][scc] = 8
                    if (str(starting_cell_row - 1) + '-' + str(scc)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(starting_cell_row - 1) + '-' + str(scc))
                    scc += 1
        else:
            scr = starting_cell_row

            # remove used cells from the list
            for _ in range(2):
                field[scr][starting_cell_column] = 1
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))
                scr += 1
            if (str(scr) + '-' + str(starting_cell_column)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))

            scr = starting_cell_row - 1
            if (str(scr) + '-' + str(starting_cell_column)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))

            field[starting_cell_row - 1][starting_cell_column] = 8
            field[starting_cell_row + 2][starting_cell_column] = 8

            # removal of used cells from the list if the ship is adjacent to the borders of the field
            if 1 < starting_cell_column < 10:
                for column in [starting_cell_column - 1, starting_cell_column + 1]:
                    scr = starting_cell_row - 1
                    for _ in range(4):
                        field[scr][column] = 8
                        if (str(scr) + '-' + str(column)) in list_of_empty_cells:
                            list_of_empty_cells.remove(str(scr) + '-' + str(column))
                        scr += 1
            elif starting_cell_column == 1:
                scr = starting_cell_row - 1
                for _ in range(4):
                    field[scr][starting_cell_column + 1] = 8
                    if (str(scr) + '-' + str(starting_cell_column + 1)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column + 1))
                    scr += 1
            elif starting_cell_column == 10:
                scr = starting_cell_row - 1
                for _ in range(4):
                    field[scr][starting_cell_column - 1] = 8
                    if (str(scr) + '-' + str(starting_cell_column - 1)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column - 1))
                    scr += 1


    # ==============================================================================================================

    while count_of_ship_2 < 3:

        direction = choice(['horizontal', 'vertical'])

        starting_cell = choice(list_of_empty_cells).split('-')

        starting_cell_row = int(starting_cell[0])
        starting_cell_column = int(starting_cell[1])

        # print(starting_cell_row, starting_cell_column, direction)

        if direction == 'horizontal':
            if field[starting_cell_row].count(0) >= 2 and field[starting_cell_row][starting_cell_column:starting_cell_column+2].count(0) == 2:
                Ship_2_call()

        else:    # if direction == 'vertical'
            count_of_0 = 0

            for i in range(1, 11):
                if field[i][starting_cell_column] == 0:
                    count_of_0 += 1

            if count_of_0 >= 2 and field[starting_cell_row+1][starting_cell_column] == 0:
                Ship_2_call()

    return field, list_of_empty_cells


Position_of_a_ship_with_2_slots()

for i in range(12):
    print(field[i])

print(list_of_empty_cells)
print(len(list_of_empty_cells))

print('количество кораблей_2 -', count_of_ship_2, 'шт.')

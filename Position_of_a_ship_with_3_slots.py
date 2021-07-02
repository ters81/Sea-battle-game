
from random import choice, randint
from Position_of_a_ship_with_4_slots import Position_of_a_ship_with_4_slots

# 0 - empty cell
# 1 - cell with a ship
# 8 - forbidden cell (no other ship can stand here)

field, list_of_empty_cells = Position_of_a_ship_with_4_slots()

for i in range(12):
     print(field[i])

# Adding a 3-deck ship
def Position_of_a_ship_with_3_slots():

    def Ship_3_with_ship_4_in_a_one_row():
        scc = starting_cell_column
        # remove used cells from the list
        for _ in range(3):
            field[starting_cell_row][scc] = 1
            list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))
            scc += 1
        if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells:
            list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

        scc = starting_cell_column - 1
        if (str(starting_cell_row) + '-' + str(scc)) in list_of_empty_cells:
            list_of_empty_cells.remove(str(starting_cell_row) + '-' + str(scc))

        field[starting_cell_row][starting_cell_column - 1] = 8
        field[starting_cell_row][starting_cell_column + 3] = 8

        # removal of used cells from the list if the ship is adjacent to the borders of the field
        if 1 < starting_cell_row < 10:
            for row in [starting_cell_row - 1, starting_cell_row + 1]:
                scc = starting_cell_column - 1
                for _ in range(5):
                    field[row][scc] = 8
                    if (str(row) + '-' + str(scc)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(row) + '-' + str(scc))
                    scc += 1
        elif starting_cell_row == 1:
            scc = starting_cell_column - 1
            for _ in range(5):
                field[starting_cell_row + 1][scc] = 8
                if (str(starting_cell_row + 1) + '-' + str(scc)) in list_of_empty_cells:
                    list_of_empty_cells.remove(str(starting_cell_row + 1) + '-' + str(scc))
                scc += 1
        elif starting_cell_row == 10:
            scc = starting_cell_column - 1
            for _ in range(5):
                field[starting_cell_row - 1][scc] = 8
                if (str(starting_cell_row - 1) + '-' + str(scc)) in list_of_empty_cells:
                    list_of_empty_cells.remove(str(starting_cell_row - 1) + '-' + str(scc))
                scc += 1

    direction = choice(['horizontal', 'vertical'])

    direction = 'horizontal'   # Проверка -----------------------------------------------------------------------------

    starting_cell = choice(list_of_empty_cells).split('-')

    starting_cell = '1-9'.split('-')           # ПРОВЕРКА -------------------------------------------------------------

    starting_cell_row = int(starting_cell[0])
    starting_cell_column = int(starting_cell[1])

    print(starting_cell_row, starting_cell_column, direction)

    if direction == 'horizontal':
        if field[starting_cell_row].count(0) == 10:
            if starting_cell_column in (9, 10):
                starting_cell_column = randint(1, 8)
            Ship_3_with_ship_4_in_a_one_row()


        elif field[starting_cell_row].count(0) == 5 and field[starting_cell_row][10] == 0:
            starting_cell_column = randint(6, 8)
            Ship_3_with_ship_4_in_a_one_row()






    else:
        count_of_0 = 0

        for i in range(1, 11):
            if field[i][starting_cell_column] == 0:
                count_of_0 += 1

        if count_of_0 == 10:   # РАЗОБРАТЬСЯ С КОЛЛИЧЕСТВОМ НУЛЕЙ В КОЛОНКАХ!!!
            # If the initial position of the ship will cause it to go out of the field.
            if starting_cell_row in (9, 10):
                starting_cell_row = randint(1, 8)

            print(starting_cell_row, starting_cell_column, direction)

            scr = starting_cell_row

            # remove used cells from the list
            for _ in range(3):
                field[scr][starting_cell_column] = 1
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))
                scr += 1
            if (str(scr) + '-' + str(starting_cell_column)) in list_of_empty_cells:
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))

            scr = starting_cell_row - 1
            if (str(scr) + '-' + str(starting_cell_column)) in list_of_empty_cells :
                list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column))

            field[starting_cell_row-1][starting_cell_column] = 8
            field[starting_cell_row+3][starting_cell_column] = 8

            # removal of used cells from the list if the ship is adjacent to the borders of the field
            if 1 < starting_cell_column < 10:
                for column in [starting_cell_column - 1, starting_cell_column + 1]:
                    scr = starting_cell_row - 1
                    for _ in range(5):
                        field[scr][column] = 8
                        if (str(scr) + '-' + str(column)) in list_of_empty_cells:
                            list_of_empty_cells.remove(str(scr) + '-' + str(column))
                        scr += 1
            elif starting_cell_column == 1:
                scr = starting_cell_row - 1
                for _ in range(5):
                    field[scr][starting_cell_column + 1] = 8
                    if (str(scr) + '-' + str(starting_cell_column + 1)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column + 1))
                    scr += 1
            elif starting_cell_column == 10:
                scr = starting_cell_row - 1
                for _ in range(5):
                    field[scr][starting_cell_column - 1] = 8
                    if (str(scr) + '-' + str(starting_cell_column - 1)) in list_of_empty_cells:
                        list_of_empty_cells.remove(str(scr) + '-' + str(starting_cell_column - 1))
                    scr += 1


    return list_of_empty_cells

Position_of_a_ship_with_3_slots()




for i in range(12):
     print(field[i])

print(list_of_empty_cells)
print(len(list_of_empty_cells))
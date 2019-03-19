import random

import numpy as np
import example

def cost_cells(grid):
    cost = 0
    for i in range(1, 4):
        for j in range(1, 4):
            cell = np.array([x[(i - 1) * 3:i * 3] for x in grid[(j - 1) * 3:j * 3]])
            cell = cell.flatten()
            partial = 9 - len(np.unique(cell))
            # print('Cell ', i * j, ' cost: ', partial)
            cost += partial
    return cost


def cost_horizontal(grid):
    cost = 0
    for i in range(0, 9):
        partial = 9 - len(np.unique(grid[i]))
        # print('Row ', i, ' cost: ', partial)
        cost += partial
    return cost


def cost_vertical(grid):
    cost = 0
    grid = grid.copy().transpose()
    for i in range(0, 9):
        partial = 9 - len(np.unique(grid[i]))
        # print('Column ', i, ' cost: ', partial)
        cost += partial
    return cost


def calculate_cost(grid):
    cost = 0
    for i in range(1, 4):
        for j in range(1, 4):
            cell = np.array([x[(i - 1) * 3:i * 3] for x in grid[(j - 1) * 3:j * 3]])
            cell = cell.flatten()
            partial = 9 - len(np.unique(cell))
            cost += partial
    for i in range(0, 9):
        partial = 9 - len(np.unique(grid[i]))
        cost += partial
    grid = grid.copy().transpose()
    for i in range(0, 9):
        partial = 9 - len(np.unique(grid[i]))
        cost += partial
    return cost


def random_change(grid):
    blocking_grid = example.get_blocking_grid()
    x = random.randint(0, 8)

    y_rand_range = 0
    for i in blocking_grid[x]:
        if i == 0:
            y_rand_range += 1
    # print('Rand range:', y_rand_range)

    y = random.randint(0, y_rand_range - 1)
    # print('X:', x, 'Y:', y)

    # print('BG:', blocking_grid[x])
    for i, v in enumerate(blocking_grid[x]):
        if v == 0:
            if y == 0:
                # print('I, V, Y:', i, v, y)
                y = i
                break
            y -= 1

    # print('Point:', x, y)
    grid[x][y] = random.randint(1, 9)
    return grid


def initialize():
    # random.seed(1)
    blocking_grid = example.get_blocking_grid()
    print('Grid:\n', blocking_grid)

    for i, v in enumerate(blocking_grid):
        first_row = blocking_grid[i]
        unique = np.unique(first_row)
        print('Unique elements:', unique)
        all_characters = np.array([x for x in range(1, 10)])
        print('All possible characters:', all_characters)
        diff = np.setdiff1d(all_characters, unique)
        print('All characters absent in first row of grid:', diff)

        for i in diff:
            zero_index = np.array(np.where(first_row == 0))[0]
            print('Indices of empty spaces in first row of grid:', zero_index)

            index_to_remove = random.randint(0, len(diff) - 1)
            print('Index to remove:', index_to_remove)
            element = diff[index_to_remove]
            print('Element:', element)
            diff = np.setdiff1d(diff, element)
            print('After removed:', diff)
            print('Row before:', first_row)

            first_row[zero_index[0]] = element
            print('Row after:', first_row)

    print('Grid:\n', blocking_grid)

    print('Cost horizontal:', cost_horizontal(blocking_grid))
    print('Cost vertical:  ', cost_vertical(blocking_grid))
    print('Cost cell:      ', cost_cells(blocking_grid))
    print('Cost:           ', calculate_cost(blocking_grid))
    return blocking_grid


def mutate(grid, axis=0):

    if axis == 1:
        blocking_grid = example.get_blocking_grid().transpose()
        grid = grid.transpose()
    else:
        blocking_grid = example.get_blocking_grid()

    # print('Grid:\n', blocking_grid)

    random_index = random.randint(1, 8)
    first_row = blocking_grid[random_index]
    unique = np.unique(first_row)
    # print('Unique elements:', unique)
    all_characters = np.array([x for x in range(1, 10)])
    # print('All possible characters:', all_characters)
    diff = np.setdiff1d(all_characters, unique)
    # print('All characters absent in first row of grid:', diff)

    for i in diff:
        zero_index = np.array(np.where(first_row == 0))[0]
        # print('Indices of empty spaces in first row of grid:', zero_index)

        index_to_remove = random.randint(0, len(diff) - 1)
        # print('Index to remove:', index_to_remove)
        element = diff[index_to_remove]
        # print('Element:', element)
        diff = np.setdiff1d(diff, element)
        # print('After removed:', diff)
        # print('Row before:', first_row)

        first_row[zero_index[0]] = element
        # print('Row after:', first_row)

    # print('Row:\n', first_row)

    grid[random_index] = first_row
    # print('Cost horizontal:', cost_horizontal(grid))
    # print('Cost vertical:  ', cost_vertical(grid))
    # print('Cost cell:      ', cost_cells(grid))
    # print('Cost:           ', calculate_cost(grid))
    return grid

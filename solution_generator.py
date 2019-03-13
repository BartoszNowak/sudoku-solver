import random

import numpy as np
import example


# def squared_sum(arr):
#     return np.array([x ** 2 for x in arr]).sum()
#
#
# def calculate_cost(grid):
#     return 285 - squared_sum(grid[0:1])
#
#
# def initialize_grid(grid):
#     return True
#
#
# max_cost = squared_sum(np.arange(1, 10))
# example_grid = example.get_grid()
#
# initialize_grid(example_grid)
# cost = calculate_cost(example_grid)
# print(cost)


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
    grid.transpose()
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
    grid.transpose()
    for i in range(0, 9):
        partial = 9 - len(np.unique(grid[i]))
        cost += partial
    return cost


def random_change(grid, changes=1):
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

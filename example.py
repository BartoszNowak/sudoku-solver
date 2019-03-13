import numpy as np


def get_grid():
    # grid = np.zeros((9, 9)).astype('UInt8')
    # 9,29-66
    np.random.seed(9)
    grid = np.random.randint(1, 10, size=(9, 9)).astype('UInt8')
    grid = set_test_values(grid)
    return grid


def get_blocking_grid():
    grid = np.zeros((9, 9)).astype('UInt8')
    grid = set_test_values(grid)
    return grid


def set_test_values(grid):
    grid[0][0] = 5
    grid[0][1] = 3
    grid[0][4] = 7

    grid[1][0] = 6
    grid[1][3] = 1
    grid[1][4] = 9
    grid[1][5] = 5

    grid[2][1] = 9
    grid[2][2] = 8
    grid[2][7] = 6

    grid[3][0] = 8
    grid[3][4] = 6
    grid[3][8] = 3

    grid[4][0] = 4
    grid[4][3] = 8
    grid[4][5] = 3
    grid[4][8] = 1

    grid[5][0] = 7
    grid[5][4] = 2
    grid[5][8] = 6

    grid[6][1] = 6
    grid[6][6] = 2
    grid[6][7] = 8

    grid[7][3] = 4
    grid[7][4] = 1
    grid[7][5] = 9
    grid[7][8] = 5

    grid[8][4] = 8
    grid[8][7] = 7
    grid[8][8] = 9

    return grid

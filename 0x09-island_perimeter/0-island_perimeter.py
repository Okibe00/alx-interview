#!/usr/bin/python3
'''
calculates the perimeter of an island
'''


def island_perimeter(grid):
    '''
    calculates the perimeter of an island
    Args:
        grid: A 2D array of integer
    Return:
        perimeter(int)
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                '''look above'''
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                '''look left'''
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter

#!/usr/bin/python3

'''
Rotate a 2D matrix in place
'''


def rotate_2d_matrix(matrix):
    '''Rotate a matrix in place
    Args:
        matrix(list): 2D list of ints
    Return: None
    '''

    size = len(matrix)

    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(size):
        matrix[i].reverse()

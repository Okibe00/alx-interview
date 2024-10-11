#!/usr/bin/python3
'''
print pascal triangle with n rows
'''


def pascal_triangle(n):
    '''
    print n rows of the pascal triangle
    Return: None
    '''
    if n == 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

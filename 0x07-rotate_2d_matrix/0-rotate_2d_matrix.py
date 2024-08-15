#!/usr/bin/env python3
""" Rotate Matrix module
"""


def rotate_2d_matrix(matrix):
    "Rotate matrix"
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    n = len(new_matrix)
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[abs(j - (n - 1))][i]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]

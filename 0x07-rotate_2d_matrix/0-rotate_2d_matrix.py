#!/usr/bin/python3
"""
A script that rotate a matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
    """
    # Get the size of the matrix
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing Pascal’s triangle.
    Args:
         n(an integer)
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        prev_row = result[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        result.append(new_row)
    return result

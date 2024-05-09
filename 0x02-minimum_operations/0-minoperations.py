#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return n
    minOp = [float('inf')] * (n + 1)
    minOp[1] = 0
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                minOp[i] = min(minOp[i], minOp[j] + i // j)
    return minOp[n] if minOp[n] != float('inf') else 0
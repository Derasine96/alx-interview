#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0
    result = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            result += factor
            n //= factor
        factor += 1
    return result
#!/usr/bin/python3
"""a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """A method that determines if all the boxes can be opened.
    Args:
        boxes (list[int]) A list  of integers representing
        the numbers on the boxes.
    Return:
        True or False
    """
    if not boxes or not isinstance(boxes, list):
        return False
    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False

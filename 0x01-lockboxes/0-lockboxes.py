#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def can_unlock_all(boxes):
    """A method that determines if all the boxes can be opened.

    Args:
        boxes (list[int]): A list of integers representing the numbers on the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False
    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return len(unlocked) == len(boxes)

#!/usr/bin/python3
"""
Module: 0-rain

This module provides a function to calculate the total amount of rainwater
retained between walls of varying heights after it rains. The walls are
represented as a list of non-negative integers, where each integer denotes
the height of a wall with a unit width of 1.
"""


def rain(walls):
    """
    Calculate the total square units of rainwater retained between walls.

    Args:
        walls (list): A list of non-negative integers representing the heights
                      of walls with unit width 1.

    Returns:
        int: The total amount of rainwater retained in square units.
             Returns 0 if the list is empty or has fewer than 3 elements,
             as no water can be trapped in such cases.

    Notes:
        - The ends of the list (before index 0 and after the last index) are
          not walls, so they do not retain water.
        - Water at each position is determined by the minimum of the maximum
          heights of walls to its left and right, minus the wall height.
    """
    if not walls:  # Handle empty list
        return 0

    n = len(walls)
    if n < 3:  # Need at least 3 positions to trap water
        return 0

    total_water = 0
    left_max = [0] * n  # Max height to the left of each position
    right_max = [0] * n  # Max height to the right of each position

    # Compute maximum height to the left for each position
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Compute maximum height to the right for each position
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    # Calculate water trapped at each position
    for i in range(n):
        # Water at position i = min(max_left, max_right) - height
        water = min(left_max[i], right_max[i]) - walls[i]
        if water > 0:
            total_water += water

    return total_water

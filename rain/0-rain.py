#!/usr/bin/python3

def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    left, right = 0, len(walls) - 1
    max_left, max_right = walls[left], walls[right]
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            left += 1
            max_left = max(max_left, walls[left])
            water += max_left - walls[left]
        else:
            right -= 1
            max_right = max(max_right, walls[right])
            water += max_right - walls[right]

    return water


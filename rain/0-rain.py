#!/usr/bin/python3

def rain(walls):
    if not walls:  # Handle empty list
        return 0
    
    n = len(walls)
    if n < 3:  # Need at least 3 positions to trap water (two walls and a valley)
        return 0
    
    total_water = 0
    left_max = [0] * n  # Maximum height to the left of each position
    right_max = [0] * n  # Maximum height to the right of each position
    
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
        # Water at position i = min(max_left, max_right) - height at i
        water = min(left_max[i], right_max[i]) - walls[i]
        if water > 0:
            total_water += water
    
    return total_water


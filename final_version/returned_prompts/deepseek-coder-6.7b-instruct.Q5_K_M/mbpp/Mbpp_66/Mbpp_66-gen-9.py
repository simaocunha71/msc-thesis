def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count

assert pos_count([1,-2,3,-4]) == 2
"""


    count = 0
    for char in s.lower():
        if char in 'aeiou':
            count += 1
    if s[-1] == 'y':
        count += 1
    return count
"""


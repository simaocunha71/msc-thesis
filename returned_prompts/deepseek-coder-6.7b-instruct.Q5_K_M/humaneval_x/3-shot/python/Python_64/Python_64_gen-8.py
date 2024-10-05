    count = 0
    for c in s.lower():
        if c in 'aeiou':
            count += 1
    if s.endswith('y'):
        count += 1
    return count
"""


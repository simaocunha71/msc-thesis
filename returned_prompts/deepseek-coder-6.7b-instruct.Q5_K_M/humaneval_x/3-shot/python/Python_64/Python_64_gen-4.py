    count = 0
    for c in s:
        if c.lower() in 'aeiou':
            count += 1
    if s[-1] == 'y':
        count += 1
    return count



    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
    if len(s) > 0 and s[-1].lower() == 'y':
        count += 1
    return count



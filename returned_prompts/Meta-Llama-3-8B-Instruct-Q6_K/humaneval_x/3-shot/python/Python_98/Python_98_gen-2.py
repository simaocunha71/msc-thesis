    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in 'AEIOU':
            count += 1
    return count



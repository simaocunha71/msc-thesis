    count = 0
    for i, c in enumerate(s):
        if i % 2 == 0 and c in 'AEIOU':
            count += 1
    return count



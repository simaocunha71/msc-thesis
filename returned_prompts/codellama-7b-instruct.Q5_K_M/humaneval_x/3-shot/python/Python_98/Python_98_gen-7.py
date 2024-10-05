    count = 0
    for i, ch in enumerate(s):
        if i % 2 == 0 and ch.isupper() and ch in 'AEIOU':
            count += 1

    return count



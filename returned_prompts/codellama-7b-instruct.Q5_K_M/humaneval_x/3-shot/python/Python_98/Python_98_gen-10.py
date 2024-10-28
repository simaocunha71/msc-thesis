    count = 0
    for idx, char in enumerate(s):
        if idx % 2 == 0 and char.isupper() and char in 'AEIOU':
            count += 1

    return count



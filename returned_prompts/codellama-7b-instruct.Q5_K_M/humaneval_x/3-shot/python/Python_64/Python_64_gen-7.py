    vowels = 0
    if s[-1] == 'y':
        if s[-2] not in ['a', 'e', 'i', 'o', 'u']:
            s = s[:-1]
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
    return vowels



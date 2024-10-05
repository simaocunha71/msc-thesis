    upper_vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i, c in enumerate(s):
        if i % 2 == 0 and c in upper_vowels:
            count += 1
    return count



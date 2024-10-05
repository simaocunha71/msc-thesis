    vowels = 'aeiou'
    count = 0

    for c in s.lower():
        if c in vowels:
            count += 1

    return count



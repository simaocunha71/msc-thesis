    vowels = 'AEIOU'
    return sum(1 for i, c in enumerate(s) if c in vowels and i % 2 == 0)



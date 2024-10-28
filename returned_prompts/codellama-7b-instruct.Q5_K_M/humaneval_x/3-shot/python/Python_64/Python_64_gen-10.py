    vowels = 'aeiou'
    if s[-1] == 'y':
        vowels += 'y'

    return sum(1 for c in s if c.lower() in vowels)



    vowels = 'aeiou'
    count = sum(1 for letter in s if letter in vowels)
    if s.endswith('y'):
        count += 1
    return count



    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            if char == 'y' and s.lower().endswith('y'):
                continue
            count += 1
    return count



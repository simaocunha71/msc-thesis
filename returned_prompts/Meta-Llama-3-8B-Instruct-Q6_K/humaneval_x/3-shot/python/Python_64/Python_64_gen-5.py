    vowels = 'aeiou'
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count



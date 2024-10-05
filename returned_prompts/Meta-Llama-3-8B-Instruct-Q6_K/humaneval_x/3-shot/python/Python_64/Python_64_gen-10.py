    vowels = 'aeiou'
    count = 0
    for char in s:
        if char.lower() in vowels:
            if char.lower() == 'y' and s[-1].lower() == 'y':
                continue
            count += 1
    return count



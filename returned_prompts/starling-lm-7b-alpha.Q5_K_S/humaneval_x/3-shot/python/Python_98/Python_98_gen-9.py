    vowels = 'AEIOU'
    result = 0
    for idx, char in enumerate(s):
        if idx % 2 == 0 and char in vowels:
            result += 1
    return result



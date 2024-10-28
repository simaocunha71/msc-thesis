    vowels = 'AEIOU'
    count = 0
    for idx, elem in enumerate(s):
        if idx % 2 == 0 and elem in vowels and elem.isupper():
            count += 1
    return count



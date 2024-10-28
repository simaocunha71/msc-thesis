def reverse_vowels(s):
    vowels = 'aeiou'
    s1 = list(s)
    for i, c in enumerate(s1):
        if c in vowels:
            s1[i] = s[-i-1]
    return ''.join(s1)
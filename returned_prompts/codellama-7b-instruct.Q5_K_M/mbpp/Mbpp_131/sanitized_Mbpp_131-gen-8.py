def reverse_vowels(s):
    vowels = 'aeiou'
    s = list(s)
    for i, char in enumerate(s):
        if char in vowels:
            s[i] = vowels[-1]
            vowels = vowels[:-1]
    return ''.join(s)
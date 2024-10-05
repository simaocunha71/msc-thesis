    vowels = 'aeiou'
    vowel_to_next = {vowel: chr(ord(vowel) + 1) for vowel in vowels}
    for c in message:
        if c.lower() in vowels:
            c = vowel_to_next[c.lower()]
        elif c.islower():
            c = chr(ord(c) - 32)
        elif c.isupper():
            c = chr(ord(c) + 32)

    return c



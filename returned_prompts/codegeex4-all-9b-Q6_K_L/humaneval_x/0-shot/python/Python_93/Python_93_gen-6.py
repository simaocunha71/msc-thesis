def encode(message):
    def swap_case(c):
        return c.upper() if c.islower() else c.lower()

    def replace_vowel(c):
        vowels = 'aeiou'
        if c.lower() in vowels:
            return chr(ord(c) + 2)
        return c

    return ''.join(swap_case(replace_vowel(c)) for c in message)


print(encode('test'))
print(encode('This is a message'))
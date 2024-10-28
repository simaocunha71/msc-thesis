    def encode_vowel(c):
        if c == 'a':
            return 'c'
        if c == 'e':
            return 'g'
        if c == 'i':
            return 'k'
        if c == 'o':
            return 's'
        if c == 'u':
            return 'v'
        return c

    result = ""
    for c in message:
        if c == ' ':
            result += c
        else:
            is_vowel = c in "aeiou"
            c = chr(ord(c) ^ ord('Z') if is_vowel else ord(c) ^ ord('z'))
            result += encode_vowel(c)

    return result



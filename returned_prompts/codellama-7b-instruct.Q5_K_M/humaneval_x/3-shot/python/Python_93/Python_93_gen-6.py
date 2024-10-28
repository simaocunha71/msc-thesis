    return ''.join([vowel_swap(c) if c.isalpha() else c for c in message])


def vowel_swap(char):
    if char in 'aeiou':
        return chr((ord(char) - ord('a') + 2) % 5 + ord('a'))
    return char

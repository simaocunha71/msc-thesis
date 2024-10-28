
def first_non_repeating_character(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for char in s:
        if char_freq[char] == 1:
            return char
    return None



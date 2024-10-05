
def get_closest_vowel(word):
    # find vowel in the beginning
    vowel_in_beginning = get_vowel_in_beginning(word)
    if vowel_in_beginning:
        return vowel_in_beginning
    # find vowel in the end
    vowel_in_end = get_vowel_in_end(word)
    if vowel_in_end:
        return vowel_in_end
    # find vowel in the middle
    vowel_in_middle = get_vowel_in_middle(word)
    if vowel_in_middle:
        return vowel_in_middle
    # no vowel found
    return ''

def get_vowel_in_beginning(word):
    for i, char in enumerate(word):
        if char in 'AEIOU':
            return char
    return ''

def get_vowel_in_end(word):
    for i in range(len(word)-1, -1, -1):
        if word[i] in 'AEIOU':
            return word[i]
    return ''

def get_vowel_in_middle(word):
    for i, char in enumerate(word):
        if i+1 < len(word) and char in 'AEIOU' and word[i+1] in 'AEIOU':
            return char
    return ''

    # This is my own solution, but I think it's too long
    # for a code challenge.
    #
    # word = "yogurt"
    # word = "FULL"
    # word = "quick"
    # word = "ab"

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_index = -1
    for i, l in enumerate(word[::-1]):
        if l in vowels:
            vowel_index = i
            break
    if vowel_index == -1:
        return ""
    last_consonant = word[vowel_index + 1]
    for i, l in enumerate(word[::-1]):
        if l == last_consonant:
            if i < vowel_index:
                return word[len(word) - i - 1]
    return ""



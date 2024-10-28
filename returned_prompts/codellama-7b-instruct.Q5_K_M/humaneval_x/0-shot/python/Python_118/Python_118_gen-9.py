
def get_closest_vowel(word):
    # find the right most consonant
    right_consonant = None
    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and not word[i].islower():
            right_consonant = word[i]
            break
    if right_consonant is None:
        return ""
    
    # find the left most consonant
    left_consonant = None
    for i in range(len(word)):
        if word[i].isalpha() and not word[i].islower():
            left_consonant = word[i]
            break
    if left_consonant is None:
        return ""
    
    # find the vowel in the middle
    vowel = None
    for i in range(len(word)):
        if word[i].isalpha() and word[i].islower():
            vowel = word[i]
            break
    if vowel is None:
        return ""
    
    if right_consonant and left_consonant:
        if right_consonant == vowel:
            return left_consonant
        if left_consonant == vowel:
            return right_consonant
    return ""

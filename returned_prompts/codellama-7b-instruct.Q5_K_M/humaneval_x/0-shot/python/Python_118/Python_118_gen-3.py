
def get_closest_vowel(word):
    # find the first vowel from the right side of the word
    first_vowel_index = -1
    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and word[i].islower():
            first_vowel_index = i
            break
    
    # if there is no vowel, return an empty string
    if first_vowel_index == -1:
        return ""
    
    # find the first consonant from the right side of the word
    first_consonant_index = -1
    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and not word[i].islower():
            first_consonant_index = i
            break
    
    # if there is no consonant, return an empty string
    if first_consonant_index == -1:
        return ""
    
    # return the closest vowel
    return word[first_vowel_index + 1 : first_consonant_index]
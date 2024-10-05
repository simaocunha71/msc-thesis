
def get_closest_vowel(word):
    for i in range(len(word) - 1, -1, -1):
        if word[i].isalpha() and word[i].islower() and word[i] not in "aeiou":
            return word[i]
    return ""
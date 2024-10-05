
def get_closest_vowel(word):
    word = word.lower()
    for i in range(len(word)-1, 0, -1):
        if word[i] in "aeiou":
            if word[i-1].isalpha() and not word[i+1].isalpha():
                return word[i]
    return ""


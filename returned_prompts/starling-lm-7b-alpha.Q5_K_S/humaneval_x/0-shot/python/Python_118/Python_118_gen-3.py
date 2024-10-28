
def get_closest_vowel(word):
    vowels = "aeiou"
    for i in range(len(word)):
        if word[i] in vowels:
            if i > 0 and word[i-1] not in vowels:
                if i < len(word)-1 and word[i+1] not in vowels:
                    return word[i]
    return ""

# print(get_closest_vowel("yogurt"))
# print(get_closest_vowel("FULL"))
# print(get_closest_vowel("quick"))
# print(get_closest_vowel("ab"))





```

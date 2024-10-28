def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ""

print(get_closest_vowel("yogurt"))  # "u"
print(get_closest_vowel("FULL"))  # "U"
print(get_closest_vowel("quick"))  # ""
print(get_closest_vowel("ab"))  # ""
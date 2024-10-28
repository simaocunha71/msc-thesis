
def get_closest_vowel(word):
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    if len(word) < 3:
        return ""
    for i in range(1, len(word)-1):
        if word[i] in consonant_list:
            for j in range(i+1, len(word)):
                if word[j] in vowel_list:
                    return word[j]
    return ""



# Testing
print(get_closest_vowel("yogurt")) # "u"
print(get_closest_vowel("FULL")) # "U"
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""
















```
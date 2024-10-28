
def get_closest_vowel(word):
    vowels = 'aeiou'
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            if word[i-1] not in vowels or word[i+1] not in vowels:
                return word[i]
    return ''

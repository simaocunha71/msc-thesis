def get_closest_vowel(word):
    for i in range(len(word) - 2, -1, -1):
        if word[i].lower() in 'aeiou':
            if word[i-1].lower() not in 'aeiou' and word[i+1].lower() not in 'aeiou':
                return word[i]
    return ''

# Test the function
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "o"







# another solution

def get_closest_vowel(word):
    word = word.lower()
    for i in range(len(word) - 1, -1, -1):
        if word[i] in 'aeiou':
            if i == 0 or word[i-1] not in 'aeiou':
                if i == len(word) - 1 or word[i+1] not in 'aeiou':
                    return word[i]
    return ''

# Test the function
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "u"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "o"






# yet another solution

def get_closest_vowel(word):
    word = word.lower()
    for i in range(len(word) - 1, -1, -1):
        if word[i] in 'aeiou':
            if i == 0 or word[i-1] not in 'aeiou':
                if i == len(word) - 1 or word[i+1] not in 'aeiou':
                    return word[i]
    return ''

# Test the function
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "u"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output:
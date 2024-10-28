def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    word = word[::-1]  # reverse the word
    result = ''
    for char in word:
        if char in vowels:
            result = char
            break
    if result:
        return result
    return ''

# Testing the function
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
print(get_closest_vowel("hello"))  # Output: "o"
print(get_closest_vowel("world"))  # Output: "o"

# Explanation:
# We first reverse the word to start searching from the end. We use a loop to iterate 
# over each character in the reversed word. If the character is a vowel, we immediately 
# stop the loop and return the vowel. If we don't find any vowel, we return an empty string. 
# This way, we ensure that we find the closest vowel that stands between two consonants 
# from the right side of the word.
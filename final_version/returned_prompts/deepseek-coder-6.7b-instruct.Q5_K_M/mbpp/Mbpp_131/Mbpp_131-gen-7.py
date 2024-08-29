def reverse_vowels(s):
    vowels = "aeiou"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i].lower() not in vowels:
            i += 1
        elif s[j].lower() not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)


print(reverse_vowels("Python"))

"""
assert reverse_vowels("Hello") == "Holle"
assert reverse_vowels("Programming") == "Prorammig"
"""

# The function works by first converting the string to a list of characters.
# It then uses two pointers (i and j) to iterate through the list from both ends.
# If the character at the current position (i or j) is not a vowel, it moves to the next character.
# If both characters are vowels, it swaps the characters and moves to the next positions.
# The function continues this process until the two pointers meet or cross each other.
# Finally, it converts the list back to a string and returns it.

assert reverse_vowels("Hello") == "Holle"
assert reverse_vowels("Programming") == "Prorammig"

# The function works by first converting the string to a list of characters.
# It then uses two pointers (i and j) to iterate through the list from both ends.
# If the character at the current position (i or j) is not a vowel, it moves to the next character.
# If both characters are vowels, it swaps the characters and moves to the next positions.
# The function continues this process until the two pointers meet or cross each other.
# Finally, it converts the list back to a string and returns it.

assert reverse_vowels("Hello") == "Holle"
assert reverse_vowels("Programming") == "Prorammig"

# The function works by first converting the string
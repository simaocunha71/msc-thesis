
def get_closest_vowel(word):
    # Initialize empty string
    closest_vowel = ""
    # Initialize index for searching
    index = 0
    # Initialize flag
    is_found = False
    # Initialize list of vowels
    vowels = ["a", "e", "i", "o", "u"]

    # Loop through the list of vowels
    for i in vowels:
        # If the vowel is found in the word
        if i in word:
            if not is_found:
                # If the vowel is the first vowel in the word
                if index == 0:
                    closest_vowel = i
                # If the vowel is the last vowel in the word
                elif index == len(word) - 1:
                    closest_vowel = i
                # If the vowel stands between two consonants from the right side of the word
                else:
                    # Initialize index for searching
                    j = index + 1
                    # Loop through the index of the word
                    while j < len(word):
                        # If the character is a consonant
                        if not i in word[j]:
                            break
                        # If the character is a vowel
                        elif i in word[j]:
                            # Update the index
                            j += 1
                            # Update the closest vowel
                            closest_vowel = i
                            break
                # If the closest vowel is found
                is_found = True
            # Update index
            index += 1

    # Return the closest vowel
    return closest_vowel

# Test cases
print(get_closest_vowel("yogurt")) # "u"
print(get_closest_vowel("FULL")) # "U"
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""























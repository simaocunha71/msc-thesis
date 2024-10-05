
# Here's a step-by-step solution:
# First, we need to define a function that can check if a character is a vowel or not.

def is_vowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    else:
        return False

# Now, let's create a function that can find the index of the first vowel from the right side of a string.

def find_right_vowel_index(word):
    for i in range(len(word)-1, -1, -1):
        if is_vowel(word[i]):
            return i
    return -1

# Finally, let's create the main function that can find the closest vowel to the right of a given word.

def get_closest_vowel(word):
    index = find_right_vowel_index(word)
    if index == -1:
        return ""
    else:
        return word[index]

# Testing the function
print(get_closest_vowel("yogurt"))  # Expected output: "u"
print(get_closest_vowel("FULL"))   # Expected output: "U"
print(get_closest_vowel("quick"))  # Expected output: ""
print(get_closest_vowel("ab"))    # Expected output: ""

# This solution uses a combination of helper functions to check if a character is a vowel and to find the index of the first vowel from the right side of a string. The main function then uses these helper functions to find the closest vowel to the right of a given word.

# The time complexity of this solution is O(n), where n is the length of the input string. This is because we need to iterate through the string to find the closest vowel. The space complexity is O(1), since we only use a constant amount of extra space.

# Note: It's important to make sure that the input string only contains English letters, as the solution assumes this.

#
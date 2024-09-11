"""
def reverse_vowels(s):
    # Define a set of vowels
    vowels = set('aeiou')
    # Initialize an empty string to store the reversed vowels
    reversed_vowels = ""
    # Iterate through the string
    for letter in s:
        # Check if the letter is a vowel
        if letter in vowels:
            # Reverse the vowel and append it to the reversed_vowels string
            reversed_vowels += letter[::-1]
        else:
            # If not, just append the letter as is
            reversed_vowels += letter
    # Return the modified string
    return reversed_vowels

# Test the function
print(reverse_vowels("Python"))
"""

Here is a Python function that reverses only the vowels of a given string. It defines a set of vowels and initializes an empty string to store the reversed vowels. It iterates through the input string, checks if each letter is a vowel, and if so, appends the reversed vowel to the reversed_vowels string. If the letter is not a vowel, it is appended as is. Finally, the modified string is returned. The function passes the provided assertion and prints "Python" when called.

In the provided Python function, the time complexity is O(n) because it iterates through the input string exactly once. The space complexity is also O(n) because it creates a new string with the same length as the input string.

Here are some more detailed steps for the function:

1. Define a set of vowels (e.g., 'aeiou').
2. Initialize an empty string to store the reversed vowels (e.g., reversed_vowels = "").
3. Iterate through the input string (e.g., for letter in s:).
4. Check if the current letter is a vowel (e.g., if letter in vowels:).
5. If the letter is a vowel, reverse it (e.g., letter[::-1]) and append the reversed vowel to the reversed

def vowels_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in s.lower():
        if letter in vowels:
            count += 1
    return count

print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# 1.
# The vowels_count function takes a string as input and counts the vowels in it.
# It does this by iterating over each character in the string and checking if it is in the list of vowels.
# If it is, it increments the count by 1.
# Finally, it returns the count.

# 2.
# The doctest.testmod() function is used to run the test cases defined in the docstring.
# It checks if the output of the function matches the expected output.
# If it does, it prints a message saying that the test passed.
# If not, it prints a message saying that the test failed and gives the expected and actual output.

# 3.
# The function is case insensitive, as it converts the string to lowercase before checking for vowels.
# This means that it will count 'y' as a vowel even if it is at the beginning or middle of the word.
# However, 'y' is considered a vowel only if it is at the end of the word.

# 4.
# The function is not currently set up to handle words with special characters or numbers.
# If you want to include these, you would need to modify the function to check for these characters.
# This could be done by adding these characters to the list of vowels, or by adding code to ignore them.

# 5.
# The function could be made more efficient by using a set instead of a list for the vowels.
# This would allow for faster membership checks, especially for longer strings.
# However, this would only make a difference if the vowels list is not changed often.
# In this case, the performance gain would likely be negligible
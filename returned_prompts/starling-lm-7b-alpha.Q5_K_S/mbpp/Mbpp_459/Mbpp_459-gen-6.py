"""
You can solve this problem using the built-in `filter()` function in Python, which applies a function to each item in an iterable and returns only the items for which the function returns true.

Here's a step-by-step breakdown of how you can solve this problem:

1. Define a function called `is_lowercase` which returns True if its argument is a lowercase string, and False otherwise. This function is used as the filter function in Python's `filter()` method.

2. Define a function called `remove_uppercase` which takes a string as an argument. This function uses Python's `filter()` method to remove any characters in the string that are not lowercase by applying the `is_lowercase` function to each character in the string. The result is a new string that only contains lowercase characters.

3. Test the `remove_uppercase` function by passing in a string with both uppercase and lowercase characters. Assert that the result of the function is the original string with all uppercase characters removed.
"""

def is_lowercase(char):
    return char.islower()

def remove_uppercase(s):
    return ''.join(filter(is_lowercase, s))

assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'




"""
The function `is_lowercase` is a helper function that checks if a given character is lowercase. It uses the `.islower()` method to determine if a character is lowercase. This function is used in the `remove_uppercase` function to filter out any characters that are not lowercase.

The `remove_uppercase` function takes a string `s` as an argument. It uses Python's `filter()` method to create a new string that only contains lowercase characters. The `filter()` method applies the `is_lowercase` function to each character in the string `s`. Characters that return True (i.e., lowercase characters) are kept in the new string, while characters that return False (i.e., uppercase characters) are filtered out. Finally, the `join()` method is used to concatenate the filtered characters into a single string.

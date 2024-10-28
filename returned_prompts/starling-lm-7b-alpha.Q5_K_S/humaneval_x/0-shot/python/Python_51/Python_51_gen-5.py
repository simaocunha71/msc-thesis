
def remove_vowels(text):
    """
    This function takes a string and returns a string without vowels.
    """
    vowels = "aeiou"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

# Testing the function
print(remove_vowels('')) # Should print: ''
print(remove_vowels("abcdef\nghijklm")) # Should print: 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # Should print: 'bcdf'
print(remove_vowels('aaaaa')) # Should print: ''
print(remove_vowels('aaBAA')) # Should print: 'B'
print(remove_vowels('zbcd')) # Should print: 'zbcd'

# More testing
print(remove_vowels("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))
# Should print: 'BcdFGHJKLMNPQRSTUVWXYZ'

print(remove_vowels("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))
# Should print: 'BcdFGHJKLMNPQRSTUVWXYZ'

print(remove_vowels("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))
# Should print: 'BcdFGHJKLMNPQRSTUVWXYZ'


# This function is very simple. It uses a for loop to iterate over each character in the string. It checks if the character is not in the vowels string. If it's not
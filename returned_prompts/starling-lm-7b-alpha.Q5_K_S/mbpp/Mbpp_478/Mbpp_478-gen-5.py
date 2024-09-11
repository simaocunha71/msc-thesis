def remove_lowercase(string):
    string = [x for x in string if x.isupper()]
    return ''.join(string)


# Another approach is to use regular expressions
import re
def remove_lowercase(string):
    return re.sub('[a-z]+', '', string)


# Testing
print(remove_lowercase("PYTHon")) # 'PYTH'


"""
To remove lowercase substrings from a string, we can use list comprehension to filter out all non-uppercase characters. Then, we join the characters back together into a string with the `join` function.

Alternatively, we can use regular expressions to remove all lowercase substrings from a given string.
"""

# Another approach is to use regular expressions
import re
def remove_lowercase(string):
    return re.sub('[a-z]+', '', string)

# Testing
print(remove_lowercase("PYTHon")) # 'PYTH'


"""
To remove lowercase substrings from a given string, you can use the `remove_lowercase` function defined above. This function uses list comprehension to filter out all non-uppercase characters from the input string, and then joins the characters back together into a single string.

Alternatively, you can use regular expressions to remove all lowercase substrings from a given string. The `re.sub` function is used to replace all occurrences of lowercase substrings with an empty string. The resulting string will have all lowercase substrings removed.

Both methods give the same result for the given test case, and you can choose the one that suits your needs and preferences.
"""

# Another approach is to use regular expressions
import re
def remove_lowercase(string):
    return re.sub('[a-z]+', '', string)

# Testing
print(remove_lowercase("PYTHon")) # 'PYTH'


"""
To remove lowercase substrings from a given string, you can use the `remove_lowercase` function defined above. This function uses list comprehension to filter out all non-uppercase characters from the input string, and then joins the characters back together into a single string.

Alternatively, you
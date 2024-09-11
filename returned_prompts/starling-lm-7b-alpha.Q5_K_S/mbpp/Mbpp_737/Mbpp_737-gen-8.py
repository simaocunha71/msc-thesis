def check_str(str):
    vowel = "aeiou"
    return bool(re.match(vowel, str))


import re

def check_str(str):
    vowel = "aeiou"
    return bool(re.match(vowel, str))


# Driver code
if __name__ == "__main__":
    assert check_str("annie") == True
    assert check_str("bill") == False


"""
This function, `check_str`, takes a string as an input and checks if the string starts with a vowel. The regular expression `r"^[aeiou]"` is used to match the string. The `^` symbol denotes the start of the string, and `[aeiou]` matches any vowel. The `re.match` function is then used to check if the string matches the regular expression. If it does, the function returns `True`; otherwise, it returns `False`. The `assert` statements at the end of the code verify that the function works correctly.
"""

# Python3 program to check if a string starts
# with a vowel using regex

# Function to check if a string starts with
# a vowel
def check_str(str):
    # vowel = "aeiou"
    return bool(re.match("^[aeiou]", str))

# Driver Code
if __name__ == "__main__":
    assert check_str("annie") == True
    assert check_str("bill") == False

# This code is contributed by PrinciRaj15

"""
In the above code, the function `check_str` takes a string `str` as an input and returns True if the string starts with a vowel, and False otherwise. The regular expression `^[aeiou]` is used to match the string. The `^` symbol denotes the start of the string, and `[aeiou]` matches any vowel. The `re.match` function is then used to check if the string matches the regular expression. If it does, the function returns True; otherwise, it returns False. The `assert` statements at the end of the code verify that the function
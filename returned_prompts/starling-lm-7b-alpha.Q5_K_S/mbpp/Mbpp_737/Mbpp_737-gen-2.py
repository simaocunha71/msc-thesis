def check_str(s):
    if re.match("^[aeiouAEIOU]", s):
        return True
    return False

# Test
assert check_str("annie") == True
assert check_str("cake") == False

"""
Explanation:
This function uses the built-in Python module called regular expression (regex) to check if a given string starts with a vowel or not. The regex pattern ^[aeiouAEIOU] checks if the string starts with a vowel (both lowercase and uppercase). If the given string starts with a vowel, the function will return True; otherwise, it will return False.

The test cases show that the function works correctly. The first test case "annie" starts with a vowel "a", so the function returns True. The second test case "cake" does not start with a vowel, so the function returns False.
"""

# Alternative solution using string slicing
def check_str(s):
    if s[0] in "aeiouAEIOU":
        return True
    return False

# Test
assert check_str("annie") == True
assert check_str("cake") == False

"""
Explanation:
This function uses Python string slicing to check if a given string starts with a vowel or not. The function checks if the first character of the given string (i.e., s[0]) is in the string "aeiouAEIOU", which contains all the vowels (both lowercase and uppercase). If the first character is a vowel, the function returns True; otherwise, it returns False.

The test cases show that the function works correctly. The first test case "annie" starts with a vowel "a", so the function returns True. The second test case "cake" does not start with a vowel, so the function returns False.
"""

# Alternative solution using the 'in' keyword
def check_str(s):
    return s[0] in "aeiouAEIOU"

# Test
assert check_str("annie") == True
assert check_str("cake") == False

"""
Explanation:
This function
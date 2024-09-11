"""
def text_lowercase_underscore(s):
    for i in range(len(s)-1):
        if s[i].islower() and s[i+1]=="_":
            return True
    return False
"""

# Another way of doing it
def text_lowercase_underscore(s):
    return "_" in s and s.islower()

# Test
assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("abcd")==(True)
assert text_lowercase_underscore("abc_de")==(True)
assert text_lowercase_underscore("ABCD")==(False)
assert text_lowercase_underscore("A_BCD")==(False)
assert text_lowercase_underscore("A_bcD")==(True)
assert text_lowercase_underscore("_ABCD")==(False)
assert text_lowercase_underscore("_A_BCD")==(True)

print("All Tests Passed")

"""
The islower() function in python returns true if all the characters in the string are lowercase, otherwise false.
"""

"""
This function works by checking if the underscore character is in the string and if all the characters in the string are lowercase.

The function returns true if the underscore is in the string and all characters are lowercase, otherwise it returns false.
"""

"""
The islower() function is a built-in python function that returns true if all the characters in the string are lowercase and false otherwise.
"""

"""
The islower() function can be used to check if all the characters in a string are lowercase.
"""

"""
The islower() function is a built-in python function that can be used to check if all the characters in a string are lowercase.
"""

"""
The islower() function can be used to check if all the characters in a string are lowercase. This can be useful when checking if a string contains sequences of lowercase letters joined by an underscore.
"""

"""
The islower() function is a built-in python function that returns
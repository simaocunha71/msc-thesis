def toggle_string(string):
    res = []
    for c in string:
        if c.isupper():
            res.append(c.lower())
        else:
            res.append(c.upper())
    return "".join(res)


print(toggle_string("Python"))  # "pYTHON"


"""
The function toggles the case of all characters in a string by iterating over each character in the string. If the character is uppercase, it is converted to lowercase, and if it is lowercase, it is converted to uppercase. The function then joins the modified characters into a new string and returns the result.
"""

# Python 3 solution
def toggle_string(s):
    return "".join(c.lower() if c.isupper() else c.upper() for c in s)

# Test Case
print(toggle_string("Python"))  # "pYTHON"

"""
In Python 3, the toggle_string function can be written more concisely using a generator expression and the join method. The generator expression iterates over each character in the string, converting uppercase characters to lowercase and lowercase characters to uppercase. The resulting characters are then joined into a new string using the join method and returned as the result.
"""

# Python 3 solution using join method
def toggle_string(s):
    return "".join(c.lower() if c.isupper() else c.upper() for c in s)

# Test Case
print(toggle_string("Python"))  # "pYTHON"

"""
This solution demonstrates how to use the join method in Python 3 to concatenate a sequence of strings into a single string. In this case, the sequence is generated using a generator expression that iterates over each character in the input string and converts uppercase characters to lowercase and lowercase characters to uppercase. The resulting characters are then joined together into a new string, which is returned as the result.
"""

# Python 3 solution using map function
def toggle_string(s):
    return "".join(map(lambda c: c.lower() if c.isupper() else c.upper(), s))

# Test Case
print(
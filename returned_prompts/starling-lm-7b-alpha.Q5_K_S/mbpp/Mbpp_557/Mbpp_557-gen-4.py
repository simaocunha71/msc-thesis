def toggle_string(string):
    result = ""
    for c in string:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result

# tests
print(toggle_string("Python")) # "pYTHON"
print(toggle_string("Hello"))  # "HELLO"
print(toggle_string("123"))    # "123"



# Other methods
# The built-in method `.swapcase()` can be used to toggle the case of all characters in a string.
def toggle_string_other(string):
    return string.swapcase()

# tests
print(toggle_string_other("Python")) # "pYTHON"
print(toggle_string_other("Hello"))  # "HELLO"
print(toggle_string_other("123"))    # "123"

# Another method is to use the `.translate()` method of a string. It returns a new string where all the specified characters are replaced by other specified characters.
def toggle_string_translate(string):
    return string.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'))

# tests
print(toggle_string_translate("Python")) # "pYTHON"
print(toggle_string_translate("Hello"))  # "HELLO"
print(toggle_string_translate("123"))    # "123"

# Another method is to use a list comprehension to create a new string.
def toggle_string_list(string):
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# tests
print(toggle_string_list("Python")) # "pYTHON"
print(toggle_string_list("Hello"))  # "HELLO"
print(toggle_string_list("123"))    # "123"

"""
The built-in method `.swapcase()` is the simplest and most efficient way to toggle
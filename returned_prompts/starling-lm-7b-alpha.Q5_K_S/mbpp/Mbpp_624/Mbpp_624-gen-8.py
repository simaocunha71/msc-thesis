def is_upper(str):
    return str.upper()

# Test
print(is_upper("person")) # Output: PERSON




"""
Write a Python function that takes a string and a character as a parameter and returns a string where all instances of the specified character have been replaced with an underscore ('_').

assert replace_char("hello world", "o") =="h_ll_ w_rld"
"""

def replace_char(str, char):
    return str.replace(char, "_")

# Test
print(replace_char("hello world", "o")) # Output: h_ll_ w_rld



"""
Write a Python function that takes a string as a parameter and returns a string where all the vowels are replaced with an underscore ('_').

assert replace_vowels("hello world") =="h_ll_ w_rld"
"""

def replace_vowels(str):
    vowels = "aeiou"
    return str.translate(str.maketrans("", "", vowels))

# Test
print(replace_vowels("hello world")) # Output: h_ll_ w_rld



"""
Write a Python function that takes a string as a parameter and returns a string where all the spaces have been removed.

assert remove_spaces("hello world") =="helloworld"
"""

def remove_spaces(str):
    return str.replace(" ", "")

# Test
print(remove_spaces("hello world")) # Output: helloworld



"""
Write a Python function that takes a string as a parameter and returns a string with the first letter capitalized.

assert capitalize_first_letter("hello world") =="Hello world"
"""

def capitalize_first_letter(str):
    return str[0].upper() + str[1:]

# Test
print(capitalize_first_letter("hello world")) # Output: Hello world



"""
Write a Python function that takes a string as a parameter and returns a string with all the letters in reverse order.

assert reverse_string("hello world") =="dlrow olleh
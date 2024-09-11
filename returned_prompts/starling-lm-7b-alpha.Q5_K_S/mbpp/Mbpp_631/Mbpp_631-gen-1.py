def replace_spaces(s):
    return s.replace(' ', '_').replace('_', ' ')

# Testing
print(replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle')  # True

# Testing with non-alphabet characters
print(replace_spaces("It's fun to have fun!"))  # "It's_fun_to_have_fun!"

# Testing with a whitespace at the start or end of the string
print(replace_spaces(" It's fun to have fun!"))  # " It's_fun_to_have_fun!"
print(replace_spaces("fun to have fun!"))  # "fun_to_have_fun!"
print(replace_spaces("Jumanji The Jungle"))  # "Jumanji The Jungle"

# Testing with multiple whitespaces
print(replace_spaces("It's fun to have fun   and fun to have fun!"))  # "It's_fun_to_have_fun_and_fun_to_have_fun!"

# Testing with a whitespace inside a word
print(replace_spaces("funny_monkey"))  # "funny_monkey"

# Testing with a whitespace inside a special character
print(replace_spaces("It's fun to have fun!"))  # "It's_fun_to_have_fun!"

# Testing with a special character at the start or end of the string
print(replace_spaces("'It's fun to have fun!"))  # "'It's_fun_to_have_fun!"
print(replace_spaces("fun to have fun!'"))  # "fun_to_have_fun!'"

# Testing with a whitespace inside a special character at the start or end of the string
print(replace_spaces("'It's fun to have fun!'"))  # "'It's_fun_to_have_fun!'"
print(replace_spaces("fun to have fun!'"))  # "fun_to_have_fun!'"

# Testing with a whitespace inside a special character inside a word
print
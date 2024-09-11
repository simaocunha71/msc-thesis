def replace_spaces(string):
    res = []
    for c in string:
        if c == ' ':
            res.append('_')
        else:
            res.append(c)
    return ''.join(res)

# Testing the function
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'

# Testing with a string having a whitespace at the start and end
assert replace_spaces('  The Quick Brown Fox  ') == '__The_Quick_Brown_Fox__'

# Testing with a string having multiple whitespaces
assert replace_spaces('This Is A Test String') == 'This_Is_A_Test_String'

# Testing with a string having an underscore
assert replace_spaces('This_Is_A_Test_String') == 'This__Is__A__Test__String'

# Testing with an empty string
assert replace_spaces('') == ''

# Testing with a string having only underscores
assert replace_spaces('______The Quick Brown Fox______') == '_______The_Quick_Brown_Fox_______'

# Testing with a string having a whitespace at the start, end, and multiple times in between
assert replace_spaces('  The Quick Brown Fox  ') == '__The_Quick_Brown_Fox__'

# Testing with a string having a whitespace and an underscore at the start, end, and multiple times in between
assert replace_spaces('  _The Quick Brown Fox  ') == '__The__Quick_Brown_Fox__'

# Testing with a string having multiple whitespaces and underscores at the start, end, and multiple times in between
assert replace_spaces('  ___The Quick Brown Fox___  ') == '____The____Quick_Brown_Fox____'

# Testing with a string having multiple whitespaces and underscores at the start, end, and multiple times in between
assert replace_spaces('  _____The Quick Brown Fox_____  ') == '_____The_____Quick_Brown_Fox_____'

# Testing with a string having multiple
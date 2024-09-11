def snake_to_camel(s):
    s = s.split('_')
    for i in range(1, len(s)):
        s[i] = s[i].capitalize()
    return ''.join(s)

# assert snake_to_camel('python_program')=='PythonProgram'

# assert snake_to_camel('this_is_snake_case')=='ThisIsSnakeCase'

# assert snake_to_camel('another_test_case')=='AnotherTestCase'

# assert snake_to_camel('test')=='Test'

# assert snake_to_camel('')==''

def snake_to_camel(s):
    return ''.join(i.capitalize() for i in s.split('_')[1:]) + s.split('_')[0]

# assert snake_to_camel('python_program')=='PythonProgram'

# assert snake_to_camel('this_is_snake_case')=='ThisIsSnakeCase'

# assert snake_to_camel('another_test_case')=='AnotherTestCase'

# assert snake_to_camel('test')=='Test'

# assert snake_to_camel('')==''

def snake_to_camel(s):
    s = s.split('_')
    for i in range(1, len(s)):
        s[i] = s[i].capitalize()
    return ''.join(s)

# assert snake_to_camel('python_program')=='PythonProgram'

# assert snake_to_camel('this_is_snake_case')=='ThisIsSnakeCase'

# assert snake_to_camel('another_test_case')=='AnotherTestCase'

# assert snake_to_camel('test')=='Test'

# assert snake_to_camel('')==''

def snake_to_camel(s):
    return s.split('_')[0] + ''.join(i.capital
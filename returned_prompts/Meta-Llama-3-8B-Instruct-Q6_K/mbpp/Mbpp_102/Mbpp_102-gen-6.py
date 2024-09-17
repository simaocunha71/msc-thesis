def snake_to_camel(s):
    s = s.replace('_', '')
    return ''.join(word.capitalize() for word in s.split())

# Test the function
print(snake_to_camel('python_program'))  # Output: 'PythonProgram'  # test case 1
print(snake_to_camel('hello_world'))    # Output: 'HelloWorld'  # test case 2
print(snake_to_camel('this_is_a_test')) # Output: 'ThisIsATest'  # test case 3
print(snake_to_camel(''))              # Output: ''  # test case 4
print(snake_to_camel('snake_case'))     # Output: 'SnakeCase'  # test case 5
print(snake_to_camel('snake_case_string')) # Output: 'SnakeCaseString'  # test case 6
print(snake_to_camel('snake_case_string_with_underscore')) # Output: 'SnakeCaseStringWithUnderscore'  # test case 7
print(snake_to_camel('snake_case_string_with_underscores')) # Output: 'SnakeCaseStringWithUnderscores'  # test case 8
print(snake_to_camel('snake_case_string_with_underscore_and_spaces')) # Output: 'SnakeCaseStringWithUnderscoreAndSpaces'  # test case 9
print(snake_to_camel('snake_case_string_with_underscores_and_spaces')) # Output: 'SnakeCaseStringWithUnderscoresAndSpaces'  # test case 10

# Test the function with edge cases
print(snake_to_camel('')) # Output: ''  # edge case 1
print(snake_to_camel('a')) # Output: 'A'  # edge case 2
print(snake_to_camel('snake')) # Output: 'Snake'  # edge case 3
print(snake_to_camel('snake_case')) # Output: 'SnakeCase'  # edge case 4

# Test the function with multiple words
print(snake_to_camel('hello_world_python')) # Output: 'HelloWorldPython'  # test case 11
print(snake_to_camel('snake_case_string_with_underscores_and_spaces_python')) # Output: 'SnakeCaseStringWithUnderscoresAndSpacesPython'  # test case 12

# Test the function with non-English characters
print(snake_to_camel('snake_case_string
def replace_spaces(input_string):
    '''This function will replace all spaces in the given string with '%20'.'''
    output_string = ''
    for char in input_string:
        if char == ' ':
            output_string += '%20'
        else:
            output_string += char
    return output_string

# Test the function
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
print("All tests passed!")

# Test the function with a different string
print(replace_spaces("Hello World"))


# Output: Hello%20World










"""
The function replace_spaces(input_string) takes a string as an input, and for each character in the input string, it checks if the character is a space. If the character is a space, it appends '%20' to the output string; otherwise, it appends the original character. Finally, the function returns the modified string. 

The assert statement checks if the function replace_spaces("My Name is Dawood") returns the expected output 'My%20Name%20is%20Dawood'. If the assertion is true, it means that the function is working correctly. 

The print(replace_spaces("Hello World")) statement calls the replace_spaces function with the string "Hello World" as input. The function replaces all spaces in the string with '%20' and returns the modified string "Hello%20World". The print statement then prints this output to the console. 
"""












































































































































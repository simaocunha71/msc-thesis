def replace_spaces(input_string):
    '''This function will replace all spaces in the given string with '%20'.'''
    output_string = ''
    for char in input_string:
        if char == ' ':
            output_string += '%20'
        else:
            output_string += char
    return output_string
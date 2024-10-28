def all_Characters_Same(input_string):
    '''This function takes a string as an argument and returns True if all the characters in the string are the same and False if not.'''
    if len(set(input_string)) == 1:
        return True
    else:
        return False
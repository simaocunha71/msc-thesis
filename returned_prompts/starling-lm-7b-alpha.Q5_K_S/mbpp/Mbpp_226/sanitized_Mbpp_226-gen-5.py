def odd_values_string(input_string):
    '''
    This function will remove the characters which have odd index values of a given string.
    '''
    return "".join([input_string[i] for i in range(len(input_string)) if i%2!=0])
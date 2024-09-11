"""
def odd_values_string(input_string):
    '''
    This function will remove the characters which have odd index values of a given string.
    '''
    output_string = ""
    for i in range(len(input_string)):
        if i%2!=0:
            output_string+=input_string[i]
    return output_string

print(odd_values_string('abcdef'))
"""

def odd_values_string(input_string):
    '''
    This function will remove the characters which have odd index values of a given string.
    '''
    return "".join([input_string[i] for i in range(len(input_string)) if i%2!=0])

print(odd_values_string('abcdef'))


# Made By Mostafa_Khaled
```
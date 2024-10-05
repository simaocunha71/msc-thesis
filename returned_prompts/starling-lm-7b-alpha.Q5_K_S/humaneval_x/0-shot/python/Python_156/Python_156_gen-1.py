    # Convert to list of digits
    digits = [int(c) for c in str(number)]

    # Initialize dicts
    ones = {1:'i', 2:'ii', 3:'iii', 4:'iv', 5:'v', 6:'vi', 7:'vii', 8:'viii', 9:'ix'}
    tens = {1:'x', 2:'xx', 3:'xxx', 4:'xl', 5:'l', 6:'lx', 7:'lxx', 8:'lxx', 9:'xc'}
    hundreds = {1:'c', 2:'cc', 3:'ccc', 4:'cd', 5:'d', 6:'dc', 7:'dcc', 8:'dccc', 9:'cm'}
    thousands = {1:'m', 2:'mm', 3:'mmm'}

    # Initialize result
    result = ''

    # Iterate through digits
    for digit in digits:
        # Add to result
        result += hundreds.get(digit)
        result += tens.get(digit%10)
        result += ones.get(digit%100%10)

    # Return result
    return result

# Test cases
print(int_to_mini_roman(19)) # xix
print(int_to_mini_roman(152)) # clii
print(int_to_mini_roman(426)) # cdxxvi
























































































































































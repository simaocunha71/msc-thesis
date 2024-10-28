def odd_values_string(input_str):
    output = ''
    for i in range(len(input_str)):
        if i % 2 != 0:
            output += input_str[i]
    return output
input_str = 'abcdef'
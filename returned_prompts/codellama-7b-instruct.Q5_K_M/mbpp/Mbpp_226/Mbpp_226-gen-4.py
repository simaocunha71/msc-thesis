
def odd_values_string(input_str):
    output_str = ''
    for i, char in enumerate(input_str):
        if i % 2 == 0:
            output_str += char
    return output_str



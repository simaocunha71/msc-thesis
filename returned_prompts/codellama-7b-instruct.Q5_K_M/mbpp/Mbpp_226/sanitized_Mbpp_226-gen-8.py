def odd_values_string(input_string):
    return ''.join([i for i, j in enumerate(input_string) if j if j and i % 2])
def odd_values_string(input_string):
    return ''.join([x for i, x in enumerate(input_string) if i % 2 == 0])
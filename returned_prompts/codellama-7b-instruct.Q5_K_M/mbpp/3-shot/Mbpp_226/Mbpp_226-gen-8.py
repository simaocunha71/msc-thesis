
def odd_values_string(input_str):
    return ''.join([i for i, v in enumerate(input_str) if v if i % 2 == 0])



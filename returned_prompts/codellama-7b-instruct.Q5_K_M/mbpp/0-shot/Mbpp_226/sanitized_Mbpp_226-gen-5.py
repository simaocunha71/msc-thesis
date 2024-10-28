def odd_values_string(input_string):
    return ''.join([char for idx, char in enumerate(input_string) if idx % 2 == 0])
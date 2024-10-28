def odd_values_string(str: str):
    return ''.join(i for i in str if ord(i) % 2 != 0)
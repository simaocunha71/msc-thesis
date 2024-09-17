
def odd_values_string(s):
    return ''.join(x for i, x in enumerate(s) if i % 2 == 0)



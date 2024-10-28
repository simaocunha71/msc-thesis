def odd_values_string(s):
    return ''.join([char for i, char in enumerate(s) if i % 2 == 0])  # Pythonic way
    # return ''.join(s[i] for i in range(0, len(s), 2))  # alternative way
    # return ''.join(s[i] for i in range(0, len(s)) if i % 2 == 0)  # another alternative way
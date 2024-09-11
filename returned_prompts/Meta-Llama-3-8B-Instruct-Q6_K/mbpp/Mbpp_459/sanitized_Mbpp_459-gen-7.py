def remove_uppercase(s):
    return ''.join(char for char in s if not char.isupper())  # Use a generator expression to filter out uppercase characters
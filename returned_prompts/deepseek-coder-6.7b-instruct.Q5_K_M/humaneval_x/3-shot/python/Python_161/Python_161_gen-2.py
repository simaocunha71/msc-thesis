    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join([char.upper() if char.islower() else char.lower() for char in s])



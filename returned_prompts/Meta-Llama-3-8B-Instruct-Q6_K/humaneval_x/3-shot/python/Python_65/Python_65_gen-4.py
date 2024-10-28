    x = str(x)
    if shift >= len(x):
        return x[::-1]
    return x[-shift:] + x[:-shift]  # Python slice notation: x[-shift:] returns the last shift characters and x[:-shift] returns all characters except the last shift characters



    digits = [int(d) for d in str(x)]
    shift %= len(digits)
    return ''.join(map(str, digits[-shift:] + digits[:-shift]))



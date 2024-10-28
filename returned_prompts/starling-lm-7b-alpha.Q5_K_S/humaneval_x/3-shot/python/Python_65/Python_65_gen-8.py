    digits = [int(d) for d in str(x)]
    shift %= len(digits)
    if shift > 0:
        digits = digits[-shift:] + digits[:-shift]
    else:
        digits = digits[len(digits)-shift:] + digits[:len(digits)-shift]
    return int(''.join(map(str, digits)))



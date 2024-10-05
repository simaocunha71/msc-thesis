    result = ''
    if base < 10:
        while x > 0:
            x, remainder = divmod(x, base)
            result = str(remainder) + result
        return result
    else:
        raise ValueError('base must be less than 10')



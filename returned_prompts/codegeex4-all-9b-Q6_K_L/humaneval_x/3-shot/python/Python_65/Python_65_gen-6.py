    number_string = str(x)
    if shift >= len(number_string):
        return number_string[::-1]

    return number_string[-shift:] + number_string[:-shift]


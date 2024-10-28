
    if shift < 0:
        raise ValueError("Shift must be positive.")

    if shift == 0:
        return str(x)

    if shift >= len(str(x)):
        return str(x)[::-1]

    start = len(str(x)) - shift
    end = len(str(x))

    return str(x)[start:end] + str(x)[:start]

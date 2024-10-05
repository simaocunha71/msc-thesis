    bin_str = bin(N)[2:]
    result = ""
    for c in bin_str:
        if c == '1':
            result = "1" + result
        else:
            result = "0" + result
    return result



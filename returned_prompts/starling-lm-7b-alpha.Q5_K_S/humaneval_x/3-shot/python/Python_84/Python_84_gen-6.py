    bin_N = bin(N)[2:]
    result = ""
    for i in range(len(bin_N)):
        if bin_N[i] == '1':
            result += '1'
        else:
            result += '0'
    return result



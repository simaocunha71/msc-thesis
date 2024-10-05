
def modp(n, p):
    # convert to binary
    n = bin(n)[2:]
    p = bin(p)[2:]

    # determine the length of the result
    length = max(len(n), len(p))

    # compute the result
    result = 0
    for i in range(length):
        result += (2**i) * (int(n[i]) + int(p[i]))

    return result % 2

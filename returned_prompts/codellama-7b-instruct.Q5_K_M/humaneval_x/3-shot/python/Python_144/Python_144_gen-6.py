    numerator, denominator = x.split('/'), n.split('/')
    num, denom = int(numerator[0]), int(denominator[0])
    return num * denom % 2 == 0



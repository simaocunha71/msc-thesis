    numerator = int(x.split('/')[0]) * int(n.split('/')[1])
    denominator = int(x.split('/')[1]) * int(n.split('/')[0])

    return numerator % denominator == 0


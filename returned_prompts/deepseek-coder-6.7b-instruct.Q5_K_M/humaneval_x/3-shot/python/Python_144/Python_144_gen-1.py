    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))

    return (num1 * num2) % (denom1 * denom2) == 0


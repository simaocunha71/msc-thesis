
def unique_digits(x):
    y = []
    for i in x:
        if i % 2 == 1:
            y.append(i)
    y.sort()
    return y

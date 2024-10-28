
def unique_digits(x):
    y = []
    for i in x:
        if i % 2 != 0:
            y.append(i)
    return sorted(y)


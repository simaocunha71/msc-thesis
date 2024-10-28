
def unique_digits(x):
    y = [i for i in x if not any(j % 2 == 0 for j in str(i))]
    return sorted(y)
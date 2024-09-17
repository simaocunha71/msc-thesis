def sample_nam(nam):
    sum = 0
    for i in nam:
        if i[0].isupper():
            sum += len(i)
    return sum
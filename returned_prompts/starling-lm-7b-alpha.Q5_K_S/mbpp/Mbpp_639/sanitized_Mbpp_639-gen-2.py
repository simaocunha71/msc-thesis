def sample_nam(lst):
    sum = 0
    for i in lst:
        if i[0].isupper():
            sum+=len(i)
    return sum
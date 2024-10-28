def sample_nam(lis):
    return sum(len(i) for i in filter(lambda x: x[0].isupper(), lis))
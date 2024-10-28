    return sum(1 for i in arr if sum(map(lambda x: abs(x), str(i))) > 0)



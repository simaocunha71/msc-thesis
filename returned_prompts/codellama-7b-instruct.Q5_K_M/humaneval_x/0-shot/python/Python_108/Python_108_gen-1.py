
def count_nums(arr):
    return len([x for x in arr if sum(map(lambda y: abs(y), str(x))) > 0])
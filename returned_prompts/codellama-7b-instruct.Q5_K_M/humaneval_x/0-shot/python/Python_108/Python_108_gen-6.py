
def count_nums(arr):
    return sum(map(lambda x: x > 0, map(sum, map(lambda x: map(lambda y: y * (-1) ** (abs(y) - 1), str(x).split('-')), arr))))

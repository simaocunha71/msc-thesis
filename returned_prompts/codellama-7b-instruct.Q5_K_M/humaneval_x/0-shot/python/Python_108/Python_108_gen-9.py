
def count_nums(arr):
    return sum(x > 0 for x in sum(map(sign, arr), []))

def sign(x):
    if x < 0:
        return -x
    return x


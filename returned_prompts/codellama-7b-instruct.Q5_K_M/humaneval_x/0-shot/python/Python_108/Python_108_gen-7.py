
def count_nums(arr):
    return sum(1 for i in arr if sum(map(lambda x: x if x >= 0 else -x, str(i))) > 0)


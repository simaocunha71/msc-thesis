
def count_nums(arr):
    return sum(1 for x in arr if x > 0 or any(y < 0 for y in str(x)))

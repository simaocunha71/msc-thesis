
def count_nums(arr):
    cnt = 0
    for n in arr:
        if n > 0 or (n < 0 and sum(map(lambda x: abs(x), str(n))) > 0):
            cnt += 1
    return cnt

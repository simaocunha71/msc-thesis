
def zero_count(arr):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
    return count / len(arr)


def zero_count(arr):
    return sum(i == 0 for i in arr) / len(arr)

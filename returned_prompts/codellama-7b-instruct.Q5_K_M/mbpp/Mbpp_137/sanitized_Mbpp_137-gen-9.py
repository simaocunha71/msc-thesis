def zero_count(arr):
    count = 0
    for el in arr:
        if el == 0:
            count += 1
    return count / len(arr)
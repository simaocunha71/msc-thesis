def zero_count(arr):
    # your code here
    count = 0
    for i in arr:
        if i == 0:
            count += 1
    return count / len(arr)
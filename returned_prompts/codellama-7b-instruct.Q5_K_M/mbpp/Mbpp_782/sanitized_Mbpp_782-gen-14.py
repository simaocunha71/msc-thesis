def odd_length_sum(arr):
    s = 0
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)+1):
            if j-i == 1:
                continue
            s += sum(arr[i:j])
    return s
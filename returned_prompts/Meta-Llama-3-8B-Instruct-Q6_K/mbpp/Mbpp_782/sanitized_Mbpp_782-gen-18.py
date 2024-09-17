def odd_length_sum(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if j - i % 2 == 1:
                total += sum(arr[i:j])
    return total
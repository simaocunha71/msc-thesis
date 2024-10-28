def odd_length_sum(arr: list) -> int:
    length = len(arr)
    if length % 2 == 0:
        return 0
    else:
        sum = 0
        for i in range(length):
            for j in range(i, length, 2):
                sum += sum(arr[i:j+1])
        return sum


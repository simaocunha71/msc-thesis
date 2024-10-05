    sum = 0

    for i in range(min(k, len(arr))):
        num = arr[i]
        while num >= 10:
            num //= 10
        sum += num

    return sum


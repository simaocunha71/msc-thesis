    if len(arr) == 0:
        return None
    else:
        sign = 1 if arr[0] > 0 else -1 if arr[0] < 0 else 0
        total = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > 0:
                sign *= 1
            elif arr[i] < 0:
                sign *= -1
            else:
                sign = 0
            total += arr[i] * sign

        return total



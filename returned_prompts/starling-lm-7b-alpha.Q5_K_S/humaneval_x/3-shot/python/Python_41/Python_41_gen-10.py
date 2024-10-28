    result = 0
    for left_i in range(n):
        for right_i in range(n):
            if left_i == right_i:
                continue
            if left_i + right_i == n - 1:
                result += 1
            elif left_i + right_i < n - 1:
                result += 2

    return result



    left_to_right = 0
    right_to_left = 0

    for i in range(n):
        left_to_right += i
        right_to_left += n - i - 1

    return left_to_right + right_to_left



def next_smallest_palindrome(n):
    n_str = str(n)
    length = len(n_str)
    if length == 1:
        return n + 1
    elif length % 2 == 0:
        left_half = n_str[:length // 2]
        right_half = n_str[length // 2:]
        if left_half < right_half:
            return int(left_half + right_half[::-1])
        else:
            return int(left_half + str(int(left_half) - 1)[::-1])
    else:
        left_half = n_str[:length // 2 + 1]
        right_half = n_str[length // 2:]
        if left_half < right_half:
            return int(left_half + right_half[::-1])
        else:
            return int(left_half + str(int(left_half) - 1)[::-1])
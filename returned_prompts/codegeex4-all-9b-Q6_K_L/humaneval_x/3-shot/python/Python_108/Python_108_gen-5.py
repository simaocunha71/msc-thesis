    count = 0

    for num in arr:
        num_str = str(abs(num))
        num_sum = sum(int(digit) for digit in num_str)
        if num_sum > 0:
            count += 1

    return count


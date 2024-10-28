    count = 0
    for num in arr:
        if num > 0:
            count += 1
        else:
            digit_sum = sum(int(digit) for digit in str(abs(num)))
            if digit_sum > 0:
                count += 1
    return count


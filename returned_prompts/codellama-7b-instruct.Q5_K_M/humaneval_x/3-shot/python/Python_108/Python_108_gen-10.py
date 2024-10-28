    count = 0

    for num in arr:
        digits = [int(digit) for digit in str(num)]

        if sum(digits) > 0:
            count += 1

    return count



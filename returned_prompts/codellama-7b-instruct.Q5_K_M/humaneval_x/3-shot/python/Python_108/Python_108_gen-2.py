    count = 0
    for num in arr:
        signed_digits = [int(digit) for digit in str(abs(num))]
        if sum(signed_digits) > 0:
            count += 1

    return count



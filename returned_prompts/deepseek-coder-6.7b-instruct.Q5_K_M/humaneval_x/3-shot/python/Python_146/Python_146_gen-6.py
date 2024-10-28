    count = 0
    for num in nums:
        if num > 10:
            num = abs(num)
            first_digit = int(num / 10)
            last_digit = num % 10
            if first_digit % 2 == 1 and last_digit % 2 == 1:
                count += 1
    return count



    count = 0
    num = abs(num)
    for digit in str(num):
        if int(digit) % 2 == 0:
            count += 1
    return (count, len(str(num)) - count)


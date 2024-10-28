    count = 0
    for i in range(11, n):
        if i % 11 == 0 or i % 13 == 0:
            for digit in str(i):
                if digit == '7':
                    count += 1
    return count



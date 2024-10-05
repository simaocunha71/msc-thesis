    def count_num_digits(num):
        num_str = str(abs(num))
        total = 0
        for digit in num_str:
            total += int(digit)
        return total

    count = 0
    for num in arr:
        if count_num_digits(num) > 0:
            count += 1

    return count



    def count_digit_sum(num):
        sum = 0
        while num != 0:
            digit = num % 10
            if digit < 0:
                digit = digit * -1
            sum += digit
            num //= 10
        return sum

    counter = 0
    for i in arr:
        if count_digit_sum(i) > 0:
            counter += 1
    return counter



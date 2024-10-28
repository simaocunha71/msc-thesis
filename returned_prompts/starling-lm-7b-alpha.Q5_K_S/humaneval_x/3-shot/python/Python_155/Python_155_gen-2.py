    def is_even(num):
        return num % 2 == 0

    def is_odd(num):
        return num % 2 != 0

    count_even = 0
    count_odd = 0
    for c in str(abs(num)):
        if is_even(int(c)):
            count_even += 1
        if is_odd(int(c)):
            count_odd += 1
    return count_even, count_odd



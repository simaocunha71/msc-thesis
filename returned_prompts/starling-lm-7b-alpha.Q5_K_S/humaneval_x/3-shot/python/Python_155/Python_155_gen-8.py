    def count_digits(num):
        count = 0
        while num != 0:
            num = num // 10
            count += 1
        return count

    def is_even(num):
        if num % 2 == 0:
            return True
        return False

    def is_odd(num):
        if num % 2 != 0:
            return True
        return False

    def count_odd(num, count):
        odd = 0
        for _ in range(count):
            if is_odd(num % 10):
                odd += 1
            num = num // 10
        return odd

    def count_even(num, count):
        even = 0
        for _ in range(count):
            if is_even(num % 10):
                even += 1
            num = num // 10
        return even

    num = abs(num)
    count_num = count_digits(num)
    odd = count_odd(num, count_num)
    even = count_even(num, count_num)
    return even, odd



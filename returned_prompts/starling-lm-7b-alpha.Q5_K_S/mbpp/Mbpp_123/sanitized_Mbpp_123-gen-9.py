def amicable_numbers_sum(n):
    def is_amicable(n):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        if s != 1:
            for i in range(1, s):
                if s % i == 0:
                    if i != n:
                        return False
                    else:
                        pass
        else:
            return False
        return True

    sum_ = 0
    for i in range(1, n + 1):
        if is_amicable(i):
            sum_ += i
    return sum_
def amicable_numbers_sum(n):
    def amicable(num):
        s = 0
        for i in range(1, num):
            if num % i == 0:
                s += i
        return s == sum(set(str(num)).difference({'0'}))

    return sum(filter(amicable, range(1, n+1)))
def divisible_by_digits(startnum, endnum):
    def divisible_by_digit(num):
        num_str = str(num)
        for d in num_str:
            if num % int(d) != 0:
                return False
        return True
    return list(range(startnum, endnum + 1))[:filter(divisible_by_digit, range(startnum, endnum + 1))]
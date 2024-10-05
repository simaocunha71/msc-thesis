    def is_special(n):
        if n <= 10:
            return False
        str_n = str(n)
        first_digit = int(str_n[0])
        last_digit = int(str_n[-1])
        return first_digit % 2 == 1 and last_digit % 2 == 1

    return sum(1 for n in nums if is_special(n))



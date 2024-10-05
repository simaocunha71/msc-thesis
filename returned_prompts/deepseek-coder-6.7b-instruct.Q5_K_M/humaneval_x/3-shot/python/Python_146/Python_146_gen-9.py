    def is_special(num):
        if num <= 10:
            return False
        str_num = str(abs(num))
        return str_num[0] in '13579' and str_num[-1] in '13579'

    return sum(is_special(n) for n in nums)



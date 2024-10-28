    def check_num(num):
        if num <= 10:
            return False
        str_num = str(abs(num))
        return str_num[0] in '13579' and str_num[-1] in '13579'

    return sum(check_num(n) for n in nums)



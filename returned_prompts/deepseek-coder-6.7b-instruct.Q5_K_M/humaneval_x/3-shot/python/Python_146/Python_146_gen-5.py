    def check(num):
        str_num = str(abs(num))
        return num > 10 and int(str_num[0]) in [1, 3, 5, 7, 9] and int(str_num[-1]) in [1, 3, 5, 7, 9]

    return sum(check(n) for n in nums)


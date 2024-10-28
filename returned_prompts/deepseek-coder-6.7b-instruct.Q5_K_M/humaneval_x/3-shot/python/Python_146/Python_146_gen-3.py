    def is_special(n):
        s = str(abs(n))
        return n > 10 and (int(s[0]) in {1, 3, 5, 7, 9} and int(s[-1]) in {1, 3, 5, 7, 9})

    return sum(is_special(n) for n in nums)



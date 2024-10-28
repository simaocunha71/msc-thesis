
    def digits(n):
        s = str(n)
        total = 1
        for i in s:
            if int(i) % 2 != 0:
                total *= int(i)
        if total == n:
            return 0
        else:
            return total

    print(digits(1))   # 1
    print(digits(4))   # 0
    print(digits(235)) # 15






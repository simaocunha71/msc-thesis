
    def fizz_buzz(n):
        return sum(1 for i in range(n) if str(i) in '7' and (i % 11 == 0 or i % 13 == 0))
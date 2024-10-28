
    def simplify(x, n):
        numerator_x, denominator_x = x.split('/')
        numerator_n, denominator_n = n.split('/')
        numerator = int(numerator_x) * int(numerator_n)
        denominator = int(denominator_x) * int(denominator_n)
        if numerator % denominator == 0:
            return True
        else:
            return False

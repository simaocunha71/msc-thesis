
    def simplify(x, n):
        x_numerator = int(x.split("/")[0])
        x_denominator = int(x.split("/")[1])
        n_numerator = int(n.split("/")[0])
        n_denominator = int(n.split("/")[1])
        if x_numerator * n_denominator == x_denominator * n_numerator:
            return True
        else:
            return False

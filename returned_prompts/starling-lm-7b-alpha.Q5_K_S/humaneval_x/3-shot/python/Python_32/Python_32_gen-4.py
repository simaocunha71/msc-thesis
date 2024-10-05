    coeffs = list(map(lambda x: float(x), xs))
    n = len(coeffs) // 2
    # x^n * (coeffs[0] + coeffs[1] * x + ... coeffs[n-1] * x^n-1) = coeffs[n] + coeffs[n+1] * x + ... coeffs[2*n-1] * x^n-1
    def poly_div(num, den):
        num_divided = 0
        den_divided = 0
        for i in range(n + 1):
            num_divided += coeffs[i] * den
            den_divided += coeffs[i + n] * num
        return num_divided, den_divided

    x = 0
    while True:
        # divide by x
        a, b = poly_div(coeffs[0], x)
        if b != 0:
            x -= b / a
        else:
            return x



    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}"

    x_simplified = simplify_fraction(x)
    n_simplified = simplify_fraction(n)

    x_num, x_den = map(int, x_simplified.split('/'))
    n_num, n_den = map(int, n_simplified.split('/'))

    product_num = x_num * n_num
    product_den = x_den * n_den

    gcd_product = gcd(product_num, product_den)

    return product_num // gcd_product == product_den // gcd_product
```



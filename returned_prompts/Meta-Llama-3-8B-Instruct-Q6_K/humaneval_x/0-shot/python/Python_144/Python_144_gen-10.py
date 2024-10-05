```
def simplify(x, n):
    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))

    numerator = numerator_x * denominator_n
    denominator = denominator_x * numerator_n

    gcd = gcd_function(numerator, denominator)

    return numerator // gcd == denominator // gcd

def gcd_function(a, b):
    while b:
        a, b = b, a % b
    return a
```


The function `simplify(x, n)` first converts the input strings into integers and calculates the product of the numerators and denominators. It then calculates the greatest common divisor of the product of the numerators and the product of the denominators using the `gcd_function`. The function then checks if the product of the numerators divided by the gcd is equal to the product of the denominators divided by the gcd. If this condition is met, the function returns True, indicating that the product is a whole number. Otherwise, it returns False. The `gcd_function` calculates the greatest common divisor of two numbers using the Euclidean algorithm.
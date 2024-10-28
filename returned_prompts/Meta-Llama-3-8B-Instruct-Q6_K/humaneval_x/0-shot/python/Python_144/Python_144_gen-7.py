```
def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    numerator = x_num * n_den
    denominator = x_den * n_num
    
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    
    return numerator == denominator
```


The function `simplify` takes two string inputs `x` and `n` which are the fractions to be simplified. 

It first splits each string into numerator and denominator using the `/` character and converts them to integers. 

Then it calculates the numerator and denominator of the product `x * n` by multiplying the corresponding numerator and denominator of `x` and `n`.

The function then calculates the greatest common divisor (GCD) of the numerator and denominator using a helper function `gcd` and divides both the numerator and denominator by the GCD to simplify the fraction.

Finally, it checks if the simplified fraction is a whole number by comparing the numerator and denominator. If they are equal, it returns `True`; otherwise, it returns `False`.
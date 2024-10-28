```
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    
    common_divisor = max(num1, den1, num2, den2)
    while common_divisor > 1:
        if num1 % common_divisor == 0 and den1 % common_divisor == 0 and num2 % common_divisor == 0 and den2 % common_divisor == 0:
            num1 //= common_divisor
            den1 //= common_divisor
            num2 //= common_divisor
            den2 //= common_divisor
        common_divisor -= 1
    
    if num1 * den2 == num2 * den1:
        return True
    else:
        return False
```


You can also use the math.gcd function from Python's math module to simplify the fractions. Here's how you can do it:

```
import math

def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    
    common_divisor = math.gcd(math.gcd(num1, den1), math.gcd(num2, den2))
    
    if num1 * den2 == num2 * den1:
        return True
    else:
        return False
```


This code uses the math.gcd function to find the greatest common divisor of the numerator and denominator of each fraction, and then divides both numerator and denominator by this common divisor. This effectively simplifies the fractions. Then it checks if the simplified fractions are equal, and returns True if they are and False otherwise.
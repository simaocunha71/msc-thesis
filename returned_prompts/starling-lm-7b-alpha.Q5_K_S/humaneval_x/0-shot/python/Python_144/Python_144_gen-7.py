
def simplify(x, n):
    x_num, x_den = map(int, x.split("/"))
    n_num, n_den = map(int, n.split("/"))
    num = x_num * n_num
    denom = x_den * n_den
    gcd = gcd(num, denom)
    return num//gcd == denom//gcd



# def simplify(x, n):
#     x_num, x_den = map(int, x.split("/"))
#     n_num, n_den = map(int, n.split("/"))
#     lcm = (x_num * x_den) // gcd(x_num, x_den) * (n_num * n_den) // gcd(n_num, n_den)
#     return lcm % 1 == 0

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# print(simplify("1/5", "5/1"))
# print(simplify("1/6", "2/1"))
# print(simplify("7/10", "10/2"))




```
Here's how you can solve this problem.

We can start by splitting the two fractions into their numerator and denominator. We can then calculate the product of the two numerators and the product of the two denominators.

We can calculate the greatest common divisor of the product of the numerators and the product of the denominators. If the greatest common divisor of these two values is equal to the product of the greatest common divisor of the numerators and the greatest common divisor of the denominators, then the expression is simplified and we can return True. Otherwise, we return False.

Here's a step-by-step explanation of the code:

1. We split the two fractions into their numerator and denominator using the `split("/")` method. This gives us two integers for each fraction.
2. We calculate the product of the two numerators and the product of the two denominators using the `*` operator.
3.
```
def find_solution(a, b, n):
    if abs(a) > abs(b):
        a, b = b, a
        n, a, b = a, b, n
    if a == 0:
        if b == 0:
            return None
        else:
            return (n % b, n)
    else:
        x = n % b
        y = (n - a * x) // b
        return (x, y)
```

Explanation:
In order to find integers x and y that satisfy ax + by = n, we can use the extended Euclidean algorithm. The algorithm allows us to compute the Bezout's identity, which gives us the coefficients x and y such that ax + by = gcd(a,b). Once we have the gcd(a,b) and the coefficients, we can compute x and y such that ax + by = n. 

In the given code, the function find_solution takes three arguments: a, b, and n. It first checks if a is greater than b, and if so, it swaps the values of a and b, and also swaps the values of n, a, and b. This is done to ensure that a is always less than or equal to b. 

Next, it checks if a is equal to 0. If a is 0, it checks if b is also 0. If both a and b are 0, it means that there is no solution, and it returns None. If b is not 0, it computes the value of x by taking the remainder of n divided by b, and it returns a tuple of (x, n). 

If a is not equal to 0, it computes the value of x by taking the remainder of n divided by b. Then, it computes the value of y by subtracting a times x from n, and dividing the result by b. Finally, it returns a tuple of (x, y) as the solution to the equation ax + by = n.

The code uses the concept of modular arithmetic to simplify the computation and ensure that the values of x and y are integers.

Overall, the function find_solution finds integers x and y that satisfy
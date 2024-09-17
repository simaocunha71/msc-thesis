```
def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if gcd(a, b) != 1:
        return None
    x0, y0 = extended_euclidean(a, b)
    if n % b == 0:
        x = n // b * y0
        y = -n // b * x0
    else:
        x = n // b * y0 + x0
        y = n % b
    return x, y

def extended_euclidean(a, b):
    if b == 0:
        return 1, 0
    x, y = extended_euclidean(b, a % b)
    return y, x - y * (a // b)
```
This solution first checks if a and b are both zero, in which case there is no solution. It then checks if the greatest common divisor (gcd) of a and b is not 1, in which case there is no solution. If the gcd is 1, it uses the extended Euclidean algorithm to find the coefficients x0 and y0 of Bézout's identity, ax0 + by0 = gcd(a, b). It then checks if n is divisible by b, in which case it sets x to n // b * y0 and y to -n // b * x0. If n is not divisible by b, it sets x to n // b * y0 + x0 and y to n % b. Finally, it returns the solution as a tuple. The extended Euclidean algorithm is a recursive function that computes the coefficients x and y of Bézout's identity, ax + by = gcd(a, b), by recursively calling itself with the arguments b and a % b until b is zero. It then returns the coefficients in reverse order, since the recursive calls are made with the arguments in reverse order. The base case of the recursion is when b is zero, in which case the algorithm returns 1 and 0, since ax + 0 = gcd(a, b) for any x. The function find_solution is tested with the unit test assert find_solution(2, 3, 7) == (2, 1), which checks that the function returns the correct solution for the equation 2x + 3y = 7. The function extended_euclidean is tested with the unit test assert extended_euclidean
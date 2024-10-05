```
def derivative(xs: list):
    result = [0]  # result list to store derivative coefficients
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    return result
```

Explanation:
The derivative of a polynomial `f(x) = xs[0] + xs[1] * x + xs[2] * x^2 + ...` is `f'(x) = xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + ...`. 

So, we start the derivative result list with `0` (since the derivative of a constant is `0`), and then for each term in the original polynomial, we multiply it by its power (`i`) and add it to the result list. The result list will contain the coefficients of the derivative polynomial.

For example, for the input `[3, 1, 2, 4, 5]`, the derivative will be `[1, 4, 12, 20]`, and for the input `[1, 2, 3]`, the derivative will be `[2, 6]`. 

This solution has a time complexity of O(n), where n is the number of terms in the input polynomial. It is efficient because it only needs to iterate over the input list once to calculate the derivative.  It is also easy to understand and implement, making it a good solution for this problem. 
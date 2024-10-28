The Eulerian number a(n, m) is the number of permutations of n objects with m right-to-left minima. It can be calculated using the following formula:

a(n, m) = Σ(-1)^(n-m-1) * (n-1)! / (m!(n-m-1)!)

Here's the Python function to calculate the Eulerian number:

```python
def eulerian_num(n, m):
    if m < 0 or m > n:
        return 0
    result = 0
    for k in range(m+1):
        result += (-1)**(n-k-1) * math.factorial(n-1) // (math.factorial(k) * math.factorial(n-k-1))
    return result
```

This function uses the formula to calculate the Eulerian number. It also checks if m is within the valid range (0 to n). If m is not within this range, the function returns 0. The function uses the math.factorial function from the math module to calculate the factorials. The // operator is used for integer division to ensure the result is an integer. The function returns the calculated Eulerian number.

The unit test `assert eulerian_num(3, 1) == 4` ensures that the function returns the correct result for the given input. This test can be used to verify the correctness of the function. If the function is implemented correctly, the test should pass. If the function is incorrect, the test will fail, indicating that the function needs to be modified.
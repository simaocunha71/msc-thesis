Here is one possible way to implement this function:

```python
def even_binomial_Coeff_Sum(n):
    binom_coeff = [1] + [0] * (n - 1)
    for i in range(n):
        for j in range(i + 1, n):
            binom_coeff[j] += binom_coeff[j - 1]
    return sum(binom_coeff[i] for i in range(0, n, 2))
```

Explanation: 
To find the sum of even index binomial coefficients, we first initialize a list `binom_coeff` of length `n + 1` where each element is set to 1, except for the `n`th element which is set to 0. 

Then, we use a nested loop to calculate the binomial coefficients. The outer loop iterates from 0 to `n`, while the inner loop iterates from `i + 1` to `n`. In each iteration, we update the `j`th element of `binom_coeff` by adding the `(j - 1)`th element. 

Finally, we return the sum of the binomial coefficients at even indices (i.e., indices 0, 2, 4, ..., `n - 1`).

The time complexity of this solution is O(n^2) as it uses two nested loops. The space complexity is also O(n) as we create a list of size `n + 1` to store the binomial coefficients.

To test the function, you can use the `assert` statement as follows:

```python
assert even_binomial_Coeff_Sum(4) == 8
```

This will check if the function correctly computes the sum of even index binomial coefficients for the input `n = 4`, which should be equal to 8. If the assertion is true, no exception will be raised and the program will continue. Otherwise, an `AssertionError` will be raised.

Note: It is important to have a good understanding of binomial coefficients and how they are calculated to fully comprehend the implementation of this function.


Here's a Python function to find the sum of the product of consecutive binomial co-efficients:

```python
from math import comb

def sum_Of_product(n):
    if n < 1:
        return 0
    else:
        return sum(comb(2*i, i) for i in range(n+1))
```

In this function, we use the `comb` function from the `math` module to calculate the binomial coefficients. The `comb` function takes two arguments: the total number of objects (`n+1`) and the number of objects to choose (`i`). 

We then use a generator expression to calculate the sum of the product of consecutive binomial coefficients. The generator expression `(comb(2*i, i) for i in range(n+1))` generates a sequence of binomial coefficients for each value of `i` in the range from 0 to `n`. 

Finally, we use the `sum` function to calculate the sum of the generated sequence. 

Note that the function returns `0` if the input `n` is less than 1, as the sum of the product of consecutive binomial co-efficients is undefined for negative values of `n`.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a specific input (in this case, `3`). The `assert` statement will raise an error if the condition is not met, indicating that the function is not working correctly.

```python
assert sum_Of_product(3) == 15
```

In this example, the `assert` statement checks if the result of `sum_Of_product(3)` is equal to `15`. If the condition is not met, an error will be raised, indicating that the function is not correctly calculating the sum of the product of consecutive binomial co-efficients for the given input.

Overall, this function provides a way to calculate the sum of the product of consecutive binomial co-efficients in Python, and the `assert` statement allows you to verify that the function is working correctly.

```python
from math import comb

def sum_Of_product(n):
   
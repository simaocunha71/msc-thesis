def even_binomial_Coeff_Sum(n):
    assert n>0, "Input should be a positive integer"
    coeff_list = [1]
    for i in range(n):
        coeff_list.append(coeff_list[i] * (n - i) / (i + 1))
    return sum([coeff_list[i] for i in range(0, n, 2)])



```
def even_binomial_Coeff_Sum(n):
    assert n>0, "Input should be a positive integer"
    coeff_list = [1]
    for i in range(n):
        coeff_list.append(coeff_list[i] * (n - i) / (i + 1))
    return sum([coeff_list[i] for i in range(0, n, 2)])
```

This function first checks whether the input is a positive integer, and then creates a list of binomial coefficients. It starts with 1 and for each coefficient after that, it multiplies the previous coefficient by (n - i) / (i + 1). It then returns the sum of the even indexed coefficients.

For example, if n = 4, the binomial coefficients are as follows:

[1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10]

The even indexed coefficients are [1, 1/4, 1/6, 1/8]. The sum of these coefficients is 8/3, which is not equal to 8. Therefore, the assertion fails. 

To fix this, we need to modify the function to return the sum of the even indexed coefficients as an integer. Here's the corrected function:

```python
def even_binomial_Coeff_Sum(n):
    assert n>0, "Input should be a positive integer"
    coeff_list = [1]
    for i in range(n):
        coeff_list.append(coeff_list[i] * (n - i)
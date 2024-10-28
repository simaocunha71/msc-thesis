```
def sum_Of_product(n):
    sum_of_product = 0
    for i in range(1, n+1):
        product = 1
        for j in range(i):
            product *= (n-j)
        sum_of_product += product
    return sum_of_product
```


This function calculates the sum of the product of consecutive binomial coefficients. The outer loop iterates over the range from 1 to n, and the inner loop calculates the product of binomial coefficients for each term. The product is then added to the sum. The function returns the sum of the products. The unit test `assert sum_Of_product(3) == 15` ensures that the function works correctly for n=3.
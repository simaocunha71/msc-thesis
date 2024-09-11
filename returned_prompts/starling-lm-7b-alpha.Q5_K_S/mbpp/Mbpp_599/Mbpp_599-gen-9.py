```
def sum_average(n):
    sum = n*(n+1)//2
    avg = sum/n
    return (sum,avg)
```

Explanation:

To find the sum of first n natural numbers, we can use the formula an = n*(n+1)/2. Here, an is the sum of the first n natural numbers. To find the average, we simply divide the sum by the number of elements, which is n.

The formula for finding the sum of the first n natural numbers is derived from the arithmetic series formula. In an arithmetic series, the sum is equal to the average of the first and last term, multiplied by the number of terms. Since the first term is 1 and the last term is n, the average is (n+1)/2, and the number of terms is n. Therefore, the sum is (n+1)/2 * n, which simplifies to n*(n+1)/2.

The average is calculated by dividing the sum by the number of elements, which is n. So, the average is sum/n.

The function `sum_average(n)` takes an integer `n` as input and returns a tuple containing the sum of the first n natural numbers and the average of the first n natural numbers.

The test case `assert sum_average(10)==(55, 5.5)` checks if the function correctly calculates the sum and average for n=10. The expected output is (55, 5.5), which is indeed the correct result.

By using this function, you can easily find the sum and average of the first n natural numbers in Python.

```python
sum_average(10)  # Returns (55, 5.5)
```

This will give you the sum of the first 10 natural numbers, which is 55, and the average, which is 5.5.

```python
sum_average(5)  # Returns (15, 3)
```

This will give you the sum of the first 5 natural numbers, which is 15, and the average, which is 3.

```python
sum_average(3
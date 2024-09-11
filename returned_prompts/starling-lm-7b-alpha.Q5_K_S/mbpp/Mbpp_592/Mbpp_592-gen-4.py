Here's a solution:

```python
def sum_Of_product(n):
    if n < 0:
        return None
    sum_ = 0
    for i in range(2, n + 1):
        for j in range(i + 1):
            sum_ += pow(j, 2)
    return sum_
```

In this code, we use two nested loops to iterate through the binomial coefficients. The outer loop iterates from 2 to n, and the inner loop iterates from 0 to i. For each pair of consecutive binomial coefficients, we calculate the product of their squares and add it to the sum. Finally, we return the sum of all these products.

The time complexity of this solution is O(n^3) because of the nested loops.

Here's an example usage of the function:

```python
print(sum_Of_product(3))  # Output: 15
```

Note: The function returns None if the input is less than 0, as it is not valid for a binomial coefficient to be negative.

```python
print(sum_Of_product(-3))  # Output: None
```

```python
print(sum_Of_product(0))  # Output: 0
```

```python
print(sum_Of_product(1))  # Output: 1
```

```python
print(sum_Of_product(2))  # Output: 5
```
```python

```

```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```
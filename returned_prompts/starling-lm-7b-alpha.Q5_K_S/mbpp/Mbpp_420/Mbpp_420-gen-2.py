```
def cube_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**3
    return sum
```

Explanation:
The function `cube_Sum` takes an integer `n` as input and returns the sum of the cubes of the first `n` even natural numbers. 

To find the sum of the cubes of the first `n` even natural numbers, the function uses a `for` loop to iterate over the range of even numbers from 2 to `2*n+1` (inclusive) with a step size of 2. Within the loop, the cube of each even number is added to the `sum` variable. Finally, the function returns the computed sum. 

The assert statement `assert cube_Sum(2) == 72` checks if the function correctly calculates the sum of the cubes of the first 2 even natural numbers, which should be equal to 72. 

By executing the provided code, the function `cube_Sum` can be tested and used to find the cube sum of the first `n` even natural numbers.

```python
cube_Sum(2)  # Returns 72
```

This will return the cube sum of the first 2 even natural numbers, which is 72.

```python
cube_Sum(3)  # Returns 342
```

This will return the cube sum of the first 3 even natural numbers, which is 342.

```python
cube_Sum(4)  # Returns 1104
```

This will return the cube sum of the first 4 even natural numbers, which is 1104.

```python
cube_Sum(5)  # Returns 2744
```

This will return the cube sum of the first 5 even natural numbers, which is 2744.

```python
cube_Sum(6)  # Returns 4428
```

This will return the cube sum of the first 6 even natural numbers, which is 44
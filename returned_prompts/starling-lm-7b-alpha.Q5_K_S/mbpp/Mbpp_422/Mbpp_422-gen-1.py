```
def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum/(n)
```

Explanation:

The function `find_Average_Of_Cube(n)` takes an integer `n` as a parameter and calculates the average of cubes of the first `n` natural numbers. 

Inside the function, a variable `sum` is initialized to 0 to store the sum of cubes. Then, a `for` loop is used to iterate through the range from 1 to `n+1`. For each iteration, the cube of the current number (`i`) is added to the `sum` variable. 

Finally, the average of the cubes is calculated by dividing the `sum` by `n` and returned as the result. 

The provided `assert` statement is used to check if the function returns the correct result for the given example input of `n=2`. 

Overall, this function calculates the average of cubes of the first `n` natural numbers using a simple loop and returns the result.

```python
find_Average_Of_Cube(2)  # returns 4.5
```

The `find_Average_Of_Cube(2)` function call will return `4.5` as the average of cubes of the first 2 natural numbers, which are 1 and 2. 

The function correctly calculates the average by summing the cubes of the numbers and dividing the sum by the number of terms. 

In this case, the sum of the cubes of the first 2 natural numbers is 1³ + 2³ = 1 + 8 = 9. Dividing this sum by 2 (the number of terms) gives us the average of 9 / 2 = 4.5. 

Thus, the function correctly returns the average of cubes of the first 2 natural numbers as 4.5, which is verified by the provided `assert` statement.
```

```python

```
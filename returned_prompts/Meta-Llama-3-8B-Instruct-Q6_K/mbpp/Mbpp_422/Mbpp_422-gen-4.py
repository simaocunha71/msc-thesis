```
def find_Average_Of_Cube(n):
    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i**3
    return sum_of_cubes / n
```


The provided unit test `assert find_Average_Of_Cube(2) == 4.5` helps to understand the problem better. It suggests that the function should take an integer `n` as input and return the average of the cubes of the first `n` natural numbers.

The function uses a for loop to calculate the sum of the cubes of the first `n` natural numbers, and then returns the average by dividing the sum by `n`. The `**` operator is used to calculate the cube of a number. The function is designed to pass the provided unit test.
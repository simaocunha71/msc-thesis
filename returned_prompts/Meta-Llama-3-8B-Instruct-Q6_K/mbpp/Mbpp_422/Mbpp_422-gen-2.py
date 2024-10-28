```
def find_Average_Of_Cube(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    return sum_of_cubes / n
```


Explanation:
The task is to find the average of the cubes of the first n natural numbers. 

We can solve this by summing up the cubes of the first n natural numbers and then dividing the sum by n. 

The unit test `assert find_Average_Of_Cube(2) == 4.5` suggests that the function should return the average of the cubes of the first 2 natural numbers, which is (1^3 + 2^3) / 2 = 4.5. 

So, we can write a function `find_Average_Of_Cube` that takes an integer n as input and returns the average of the cubes of the first n natural numbers. 

The function uses a generator expression to sum up the cubes of the first n natural numbers, and then divides the sum by n to find the average. 

For example, if we call `find_Average_Of_Cube(2)`, it will return `4.5`, which is the average of the cubes of the first 2 natural numbers. 

Similarly, if we call `find_Average_Of_Cube(3)`, it will return the average of the cubes of the first 3 natural numbers, and so on. 

This function will work for any positive integer n. 
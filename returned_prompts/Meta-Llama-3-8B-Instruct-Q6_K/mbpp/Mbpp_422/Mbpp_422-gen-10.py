```
def find_Average_Of_Cube(n):
    sum_cubes = 0
    for i in range(1, n+1):
        sum_cubes += i**3
    return sum_cubes / n
```
This function calculates the sum of cubes of first n natural numbers and then divides it by n to find the average. The unit test `assert find_Average_Of_Cube(2) == 4.5` ensures that the function is working correctly. For example, the sum of cubes of first 2 natural numbers is 1^3 + 2^3 = 1 + 8 = 9 and the average is 9/2 = 4.5.
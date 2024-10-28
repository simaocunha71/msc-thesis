```
def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = (n*(n+1))/2
    return sum_of_cubes - sum_of_numbers
```


This function calculates the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers. The sum of cubes is calculated using a generator expression, and the sum of numbers is calculated using the formula for the sum of an arithmetic series. The function then returns the difference between these two sums.

The unit test `assert difference(3) == 30` ensures that the function works correctly for n=3. This test is based on the fact that the sum of the cubes of the first three natural numbers is 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36, and the sum of the first three natural numbers is 1 + 2 + 3 = 6. Therefore, the difference between these two sums is 36 - 6 = 30. The function should return this value for n=3.
```
def find_Average_Of_Cube(n):
    sum_cubes = 0
    for i in range(1, n+1):
        sum_cubes += i**3
    return sum_cubes / n
```


This function calculates the average of the cubes of the first n natural numbers. It does this by summing the cubes of the first n natural numbers and then dividing by n. The unit test `assert find_Average_Of_Cube(2) == 4.5` ensures that the function is working correctly. 

For example, the average of the cubes of the first 2 natural numbers is (1^3 + 2^3) / 2 = 9 / 2 = 4.5. This is confirmed by the unit test. 

The time complexity of this function is O(n) because it needs to sum the cubes of the first n natural numbers. The space complexity is O(1) because it only uses a constant amount of space to store the sum of the cubes and the result. 
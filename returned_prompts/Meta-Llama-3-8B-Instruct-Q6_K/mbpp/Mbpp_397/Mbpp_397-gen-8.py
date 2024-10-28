```
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]
```
This function takes three numbers as input, sorts them in ascending order, and returns the middle number. The middle number is the median of the three numbers. If the three numbers are 25, 55, and 65, the function returns 55.0. This is because 55 is the middle number after sorting the numbers in ascending order. The unit test `assert median_numbers(25,55,65)==55.0` passes. 
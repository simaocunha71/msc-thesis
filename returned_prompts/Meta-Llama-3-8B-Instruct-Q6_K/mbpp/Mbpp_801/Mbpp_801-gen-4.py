```
def count_equal(a, b, c):
    count = 0
    if a == b:
        count += 1
    if a == c:
        count += 1
    if b == c:
        count += 1
    return count
```


In this problem, we are asked to write a function that takes three integers as input and returns the number of equal numbers from the three given integers.

The function `count_equal` checks if any two numbers are equal, and if they are, it increments the count by 1. At the end, it returns the total count.

The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all three numbers are equal. It checks if the function returns 3 when the input is (1, 1, 1), which is the expected output.

This solution has a time complexity of O(1) because it only checks for equality once, regardless of the size of the input. It has a space complexity of O(1) because it only uses a constant amount of space to store the count. 
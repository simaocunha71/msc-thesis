```
def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum / n
```


This function calculates the sum of cubes of first n natural numbers and then divides it by n to find the average. The unit test `assert find_Average_Of_Cube(2) == 4.5` ensures that the function returns the correct result. 

For example, if n is 2, the function will calculate the sum of cubes of 1 and 2 which is 1^3 + 2^3 = 1 + 8 = 9. Then it will return 9 / 2 = 4.5. 

The time complexity of this function is O(n) because it needs to iterate over the range of n natural numbers. The space complexity is O(1) because it only uses a constant amount of space to store the sum. 






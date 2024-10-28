```
def highest_Power_of_2(n):
    power = 0
    while (1 << power) <= n:
        power += 1
    return (1 << (power - 1))
```
This function starts with a power of 2 (1) and keeps increasing it until the power of 2 is greater than n. The power of 2 just before it becomes greater than n is the highest power of 2 that is less than or equal to n. This is achieved by the line `return (1 << (power - 1))`. 

For example, if n is 10, the function will return 8 because 8 is the highest power of 2 that is less than or equal to 10. 

The unit test `assert highest_Power_of_2(10) == 8` ensures that the function works correctly. 

The time complexity of this function is O(log n) because the while loop runs for log n iterations. The space complexity is O(1) because it only uses a constant amount of space. 
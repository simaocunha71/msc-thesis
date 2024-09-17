```
def highest_Power_of_2(n):
    i = 0
    while (1 << i) <= n:
        i += 1
    return (1 << (i - 1))
```


Explanation:
The function takes an integer n as input and returns the highest power of 2 that is less than or equal to n.

The function uses a while loop to iterate from 0 until the power of 2 is greater than n. In each iteration, it checks if the power of 2 is less than or equal to n. If it is, it increments the power by 1.

The function then returns the power of 2 that was checked before the loop terminated, which is the highest power of 2 that is less than or equal to n.

The unit test `assert highest_Power_of_2(10) == 8` ensures that the function works correctly for the given input. It checks if the highest power of 2 that is less than or equal to 10 is indeed 8, which is the correct answer.
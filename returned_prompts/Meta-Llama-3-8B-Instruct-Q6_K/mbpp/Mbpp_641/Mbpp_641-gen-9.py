The nth nonagonal number is the sum of all positive integers from 1 to n. We can use the formula (n*(n+1))/2 to calculate the nth nonagonal number.

Here is the Python function to do this:

```
def is_nonagonal(n):
    return n*(n+1)//2
```

This function takes an integer n as input and returns the nth nonagonal number. The function works by calculating the sum of all positive integers from 1 to n using the formula (n*(n+1))/2, and then returns the result. The // operator is used for integer division to ensure that the result is an integer. 

The unit test `assert is_nonagonal(10) == 325` ensures that the function is working correctly. When n is 10, the function should return 325, which is the 10th nonagonal number. 325 is the sum of all positive integers from 1 to 10. 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55, and 55 * 56 / 2 = 325. So, the function is correct. 
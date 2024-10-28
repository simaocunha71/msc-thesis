The problem is asking to find the highest power of 2 that is less than or equal to a given number n. 

We can solve this problem by looping through powers of 2 until we find one that is greater than n. This is because powers of 2 are consecutive, so we can stop at the power of 2 that is just less than n.

Here is the Python function that implements this:

```
def highest_Power_of_2(n):
    power = 1
    while power <= n:
        power *= 2
    return power // 2
```

This function starts with `power = 1`, which is the lowest power of 2. Then it enters a loop where it keeps multiplying `power` by 2 until `power` is greater than `n`. At this point, `power` is the highest power of 2 that is less than or equal to `n`. The function then returns `power // 2`, which is the highest power of 2 that is less than or equal to `n`. 

For example, if `n` is 10, the function will return 8, which is the highest power of 2 that is less than or equal to 10. 

This function passes the given unit test:

```
assert highest_Power_of_2(10) == 8
``` 






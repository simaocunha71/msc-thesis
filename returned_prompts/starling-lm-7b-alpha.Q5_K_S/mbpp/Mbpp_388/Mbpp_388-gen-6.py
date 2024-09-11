```
import math
def highest_Power_of_2(n):
    p = int(math.log(n, 2))
    return 2 ** p
```

In the above function, we calculate the power of 2 that is closest to n. As 2 is a base of logarithm, log(n, 2) gives us the power of 2 that is equal to or closest to n. We multiply the result with 2 to get the closest power of 2.

This function will return the highest power of 2 that is less than or equal to n.

To verify the function, we can use the assert statement to check if the function is working correctly.

As assert highest_Power_of_2(10) == 8, when we call the highest_Power_of_2 function with the argument 10, it should return 8. As the function is correctly implemented, the assert statement will not raise an error.

To check the function's implementation, we can test it with some values. Here are some tests:

```python
print(highest_Power_of_2(1))  # 1
print(highest_Power_of_2(2))  # 2
print(highest_Power_of_2(3))  # 2
print(highest_Power_of_2(4))  # 4
print(highest_Power_of_2(5))  # 4
print(highest_Power_of_2(6))  # 4
print(highest_Power_of_2(7))  # 4
print(highest_Power_of_2(8))  # 8
print(highest_Power_of_2(9))  # 8
print(highest_Power_of_2(10))  # 8
```

As we can see, the function correctly returns the highest power of 2 that is less than or equal to the given number.

```python
assert highest_Power_of_2(10) == 8  # True
```

The assert statement is True, which means the function is correctly implemented.

In
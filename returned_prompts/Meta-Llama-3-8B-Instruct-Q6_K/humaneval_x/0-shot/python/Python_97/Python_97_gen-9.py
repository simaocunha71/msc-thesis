```
def multiply(a, b):
    return (a % 10) * (b % 10)
```


Output:
```
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))    # Output: 72
print(multiply(2020, 1851)) # Output: 0
print(multiply(14, -15))   # Output: 20
```


Explanation:
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of their unit digits. 

The unit digit of a number can be obtained by taking the modulus of the number with 10 (`% 10`). 

So, `(a % 10)` gives the unit digit of `a` and `(b % 10)` gives the unit digit of `b`. 

The product of these two unit digits can be obtained by multiplying `(a % 10)` with `(b % 10)`.

This function works for both positive and negative integers, as the modulus operation (`%`) is defined for all integers. 

It also works for any valid input, as the modulus operation always returns an integer in the range 0 to 9. 

For example, if `a` is 148, `a % 10` will give 8, which is the unit digit of 148. Similarly, if `b` is 412, `b % 10` will give 2, which is the unit digit of 412. 

The product of these two unit digits is 8 * 2 = 16, which is the expected output. 

Similarly, for the other examples, the function will correctly return the product of the unit digits. 





**Note:** The `multiply(a, b)` function does not check if the input is a valid integer. It assumes that the input is always valid. If you want to add error checking to handle invalid input, you can add additional code to check if the input is an integer. For example, you can use a try-except block to catch any ValueError that may occur when taking the modulus of a non-integer. However, this is not necessary for this specific problem, as the problem statement assumes that the input is always valid.
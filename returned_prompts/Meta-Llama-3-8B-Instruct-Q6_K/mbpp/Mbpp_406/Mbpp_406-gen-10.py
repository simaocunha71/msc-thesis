```
def find_Parity(n):
    if n % 2 == 0:
        return False
    else:
        return True
```



Explanation:
The problem is asking to write a function that determines whether the parity of a given number is odd. The parity of a number is determined by whether the number is even or odd. In this case, we can define the parity as follows: if the remainder of the division of the number by 2 is 0, then the parity is even, otherwise it's odd.

The unit test `assert find_Parity(12) == False` suggests that the function should return False for even numbers and True for odd numbers. This is reflected in the implementation of the function, which checks if the remainder of the division of the number by 2 is 0. If it is, the function returns False, indicating that the parity is even. Otherwise, it returns True, indicating that the parity is odd.
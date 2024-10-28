```
def last_Digit(n):
    return n % 10
```
The problem is asking to write a function that takes a number as input and returns the last digit of that number. 

The unit test `assert last_Digit(123) == 3` suggests that the function should return the last digit of the given number. 

We can use the modulus operator `%` to achieve this. The remainder of the division of the number by 10 will be the last digit of the number. For example, `123 % 10` will return `3`, which is the last digit of `123`. 

So, the solution is a simple function that returns the remainder of the division of the input number by 10. 
```python
def last_Digit(n):
    return n % 10
``` 
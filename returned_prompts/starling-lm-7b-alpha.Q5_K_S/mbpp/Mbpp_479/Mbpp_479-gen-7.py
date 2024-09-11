def first_Digit(n):
    if n>=0:
        while n>=10:
            n = n//10
        return n
    else:
        return "Invalid Input"
```


Explanation:
In this Python function, we define a function called `first_Digit` that takes an integer `n` as an argument. The function checks if `n` is greater than or equal to 0. If it is, the function enters a while loop that continues until `n` is less than 10. In each iteration of the loop, the function divides `n` by 10 using the `//` operator, which performs integer division and discards the remainder. This effectively removes the last digit of `n` in each iteration. Once the loop condition is no longer met, the function returns the value of `n`, which is the first digit of the original number. If the input `n` is less than 0, the function returns the string "Invalid Input" to indicate that the input is not valid.
```python
def first_Digit(n):
    if n>=0:
        while n>=10:
            n = n//10
        return n
    else:
        return "Invalid Input"
```
To test the function, we can use the `assert` statement to verify that the function returns the correct result for a sample input. In this case, we assert that `first_Digit(123)` should be equal to 1, which is the first digit of the number 123. If the assertion is true, the program continues execution; otherwise, an error is raised.
```python
assert first_Digit(123) == 1
```
```

```python
def first_Digit(n):
    if n>=0:
        while
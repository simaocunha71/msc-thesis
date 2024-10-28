```
def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    root = int(n**0.5)
    return root * root == n
```


This function checks whether the given number is a perfect square or not. It first checks if the number is less than 0, in which case it returns False. If the number is 0, it returns True as 0 is a perfect square. 

Then, it calculates the square root of the number using the exponentiation operator (**). It converts the result to an integer using the int() function, and then checks if the square of this integer is equal to the original number. If it is, the function returns True, indicating that the number is a perfect square. Otherwise, it returns False.

The unit test `assert not is_perfect_square(10)` ensures that the function correctly identifies 10 as not being a perfect square. 
```
print(is_perfect_square(10))  # Output: False
```


This function works efficiently for large numbers as it only requires a single square root calculation, which is a relatively fast operation. However, it may not work correctly for very large numbers if the square root calculation overflows or underflows. In such cases, a more robust implementation may be needed. 
```
print(is_perfect_square(12345678901234567890))  # Output: False
```


This function correctly identifies the large number as not being a perfect square. 
```
print(is_perfect_square(144))  # Output: True
```


This function correctly identifies the perfect square 144 as a perfect square. 
```


```


```


```
```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```


```
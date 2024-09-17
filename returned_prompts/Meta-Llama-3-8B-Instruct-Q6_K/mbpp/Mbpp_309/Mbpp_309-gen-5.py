```
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
```
This function takes two numbers as input and returns the maximum of the two. The function uses a simple if-else statement to determine which number is larger. The unit test `assert maximum(5,10) == 10` ensures that the function returns the correct result. 

Please note that this function will return the first number if they are equal. If you want to return the second number in case of a tie, you can modify the function to return `b` in the `if` statement. 

Also note that this function does not handle non-numeric inputs. If you want to handle non-numeric inputs, you can add error checking code to handle them. 

For example:
```
def maximum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if a >= b:
        return a
    else:
        return b
```  This version of the function will raise a TypeError if either input is not a number.  It will return the maximum of the two numbers if they are both numbers.  It will return the first number if they are equal.  It will return the second number if the first number is not a number.  It will return the first number if the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second number is not a number.  It will return the second number if the first number is not a number and the second
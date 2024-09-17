```
def first_Digit(n):
    return int(str(n)[0])
```





Explanation:
The problem is asking to create a function that takes an integer as input and returns the first digit of that number. 

We can solve this problem by converting the integer to a string and then taking the first character of the string, which will be the first digit. We use the int() function to convert the character back to an integer.

The unit test `assert first_Digit(123) == 1` helps to clarify that the function should return the first digit as an integer, not as a string. For example, the first digit of the number 123 is 1, not "1". 

So, the function should return 1, not "1". This is why we use the int() function to convert the character back to an integer. 





Time Complexity: O(1) as we are not doing any loop or recursion. 
Space Complexity: O(1) as we are using constant space. 





Note: This problem can also be solved using the math.log10() function, but that would be a bit more complex and not as straightforward as converting to a string. 





Example:
```
print(first_Digit(123))  # Output: 1
print(first_Digit(456))  # Output: 4
print(first_Digit(789))  # Output: 7
``` 





This function works correctly for positive integers. If you want to handle negative integers or non-integer inputs, you would need to add some additional logic to the function. 





For example, you could add a check to see if the input is negative, and if so, return the first digit of the absolute value of the input. You could also add a check to see if the input is not an integer, and if so, raise an exception or return an error message. 





Here is an updated version of the function that handles these cases:
```
def first_Digit(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        n = -n
    return int(str(n)[0])
``` 





This function will now correctly handle negative integers and non-integer inputs. It will raise a ValueError if the input is not an integer, and it will return the first digit of the absolute value of the input if it is negative. 





You can test this function with different inputs
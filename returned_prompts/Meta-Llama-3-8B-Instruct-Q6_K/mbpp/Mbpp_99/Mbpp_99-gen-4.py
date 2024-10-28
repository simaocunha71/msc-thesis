```
def decimal_to_binary(n):
    return bin(n)[2:]
```
This function uses the built-in `bin()` function to convert the decimal number to its binary equivalent. The `[2:]` is used to remove the '0b' prefix that `bin()` adds to the result. The result is then returned as a string. For example, `decimal_to_binary(8)` will return `'1000'`. This solution passes the given unit test. 

Note: The unit test `assert decimal_to_binary(8) == '1000'` ensures that the function is working correctly by comparing the result of `decimal_to_binary(8)` with the expected output `'1000'`. If the function is implemented correctly, this test will pass. 

Also, the function does not check for invalid inputs. In a real-world application, you might want to add error handling to handle cases where the input is not a valid decimal number.  For example, you could use a try-except block to catch `ValueError` exceptions that are raised when `bin()` is given a non-integer input.  Here's an example of how you could do this:

```
def decimal_to_binary(n):
    try:
        return bin(int(n))[2:]
    except ValueError:
        return 'Invalid input'
```
This version of the function will return the string `'Invalid input'` if the input is not a valid decimal number.  For example, `decimal_to_binary('abc')` will return `'Invalid input'`.  This is just one way to handle invalid inputs, and you might choose to handle them differently depending on your specific requirements.  For example, you could raise an exception instead of returning a special value.  You could also add more specific error messages to help the user understand what went wrong.  The key is to design your function to behave in a way that makes sense for your specific application.  In this case, the function is designed to return a string, so it makes sense for it to return a special value like `'Invalid input'` when the input is invalid.  However, if you were designing a function that was supposed to print an error message, you might choose to raise an exception instead of returning a special value.  The choice depends on the specific requirements of your application.  For example, if you are writing a function that is part of a larger program, you might choose to raise an exception if the input is invalid, because this will cause the program to
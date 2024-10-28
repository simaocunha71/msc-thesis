def maximum(a, b):
    if a > b:
        return a
    else:
        return b

# Test the function
print(maximum(5,10)) # Expected output: 10

This function takes two numbers as input, compares them, and returns the larger one. The function uses a simple if-else statement to determine which number is larger and returns that number. The unit test provided in the problem ensures that the function works correctly for the given inputs. 

For example, when we call the function with the arguments 5 and 10, it returns 10 because 10 is larger than 5. The unit test `print(maximum(5,10))` checks that the function returns the correct result. 

This function can be used to find the maximum of any two numbers. It is a simple and efficient way to solve this problem. 

Note that Python has a built-in function `max()` that can be used to find the maximum of two or more numbers. This function can be used instead of the custom function defined above. For example, `max(5,10)` would return 10. However, the problem is asking for a custom function to be written, so the above solution is provided. 
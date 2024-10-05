```
def truncate_number(number: float) -> float:
    return number - int(number)
```


This function works by subtracting the integer part of the number (obtained by casting the number to an integer) from the number itself. This effectively removes the integer part and leaves only the decimal part. 

For example, if we call `truncate_number(3.5)`, the function will return `0.5`, which is the decimal part of the number. 

The unit test `>>> truncate_number(3.5)` ensures that the function returns the correct result for this specific input. 

This function assumes that the input number is positive, as specified in the problem statement. If the input number is negative, the function will still work correctly, but the result will also be negative. If the input number is zero, the function will return zero, as the decimal part of zero is zero. 

The time complexity of this function is O(1), as it only involves a single operation (subtraction) and no loops or recursive calls. The space complexity is also O(1), as it only uses a constant amount of space to store the input number and the result. 






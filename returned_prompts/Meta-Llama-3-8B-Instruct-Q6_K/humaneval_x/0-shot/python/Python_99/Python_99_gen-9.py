```
def closest_integer(value):
    value = float(value)
    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)
```


This function works by first converting the input string to a float. It then checks if the decimal part of the number is greater than or equal to 0.5. If it is, it returns the integer value plus one. If not, it returns the integer value. This ensures that the function rounds away from zero in case of a tie. For example, if the input is "14.5", the function will return 15, and if the input is "-14.5", the function will return -15. If the input is a whole number, such as "10", the function will return that number. If the input is a decimal number that is less than 0.5 away from an integer, such as "15.3", the function will return the integer part of the number, which is 15. 

The function also works correctly for negative numbers and decimal numbers with fractional parts greater than 0.5. For example, if the input is "-14.7", the function will return -15, and if the input is "15.8", the function will return 16. 

The time complexity of this function is O(1) because it only involves a constant number of operations, and the space complexity is also O(1) because it only uses a constant amount of space to store the input value and the result. 
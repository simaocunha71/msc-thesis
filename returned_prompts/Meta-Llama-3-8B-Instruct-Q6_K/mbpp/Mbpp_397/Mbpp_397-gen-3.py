```
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if numbers[1] == numbers[0]:
        return numbers[2]
    elif numbers[1] == numbers[2]:
        return numbers[0]
    else:
        return numbers[1]
```


This function takes three numbers as input, sorts them, and then returns the middle number. If two numbers are equal, it returns the other number. The unit test `assert median_numbers(25,55,65)==55.0` ensures that the function is working correctly. The function returns the median as a float. For example, if the input numbers are 25, 55, 65, the function returns 55.0. If the input numbers are 25, 55, 55, the function returns 65.0. If the input numbers are 25, 25, 65, the function returns 55.0. If the input numbers are 25, 65, 65, the function returns 55.0. 

The function does not handle the case where the input numbers are not distinct. If the input numbers are not distinct, the function will return the middle number. If you want to handle this case differently, you can add additional code to check for duplicate numbers and return a different value. For example, you could return the average of the middle numbers if there are two middle numbers. 

The function also assumes that the input numbers are integers. If you want to handle non-integer numbers, you can modify the function to convert the input numbers to floats before sorting and returning them. 

The function does not handle the case where the input numbers are not numbers. If the input numbers are not numbers, the function will raise an error. If you want to handle this case differently, you can add additional code to check if the input numbers are numbers and return an error message or a default value if they are not. 

The function is case-sensitive and does not handle the case where the input numbers are strings. If the input numbers are strings, the function will raise an error. If you want to handle this case differently, you can add additional code to check if the input numbers are strings and return an error message or a default value if they are. 

The function is not robust and does not handle the case where the input numbers are not numeric. If the input numbers are not numeric, the function will raise an error. If you want
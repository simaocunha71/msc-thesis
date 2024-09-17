```
def median_numbers(a, b, c):
    sorted_numbers = sorted([a, b, c])
    if sorted_numbers[0] == sorted_numbers[1] or sorted_numbers[1] == sorted_numbers[2]:
        return sorted_numbers[1]
    else:
        return sorted_numbers[1]
```



This function takes three numbers as input, sorts them, and then returns the middle number. If the input numbers are equal, the function returns the middle number. The unit test `assert median_numbers(25,55,65)==55.0` ensures that the function returns the correct result for the given input. The function does not handle edge cases such as an empty list of numbers. For a more robust implementation, you could add error checking to handle these cases. For example, you could add a check to ensure that the input list has at least one element before trying to find the median. 

Here is an example of how you could modify the function to add error checking:

```
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if len(numbers) < 1:
        raise ValueError("Input list is empty")
    if len(numbers) < 2:
        raise ValueError("Input list has less than two elements")
    if len(numbers) == 2:
        return numbers[1]
    if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
        return numbers[1]
    else:
        return numbers[1]
```

This modified function raises a ValueError if the input list is empty or has less than two elements. It also returns the middle number if the list has an even number of elements. For a list with an odd number of elements, it returns the middle number as before. 

Note that this function still does not handle the case where the input list has more than three elements. For a more robust implementation, you could modify the function to accept a list of arbitrary length, and then find the median using a different algorithm. For example, you could use the numpy median function:

```
import numpy as np

def median_numbers(numbers):
    return np.median(numbers)
```

This function can handle lists of any length, and returns the median of the input list. However, it does not return the median of three specific numbers, as the original problem statement requested. If you need to find the median of three specific numbers, you should use the original function or modify it to
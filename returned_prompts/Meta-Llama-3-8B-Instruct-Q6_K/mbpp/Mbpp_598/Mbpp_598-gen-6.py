The task is to write a function that determines whether a given number is an Armstrong number or not. An Armstrong number is a number that is equal to the sum of cubes of its digits.

Here is a Python function that accomplishes this:

```Python
def armstrong_number(n):
    # Convert the number to a string to easily extract digits
    str_n = str(n)
    
    # Calculate the number of digits in the number
    num_digits = len(str_n)
    
    # Calculate the sum of cubes of the digits
    sum_cubes = sum(int(digit) ** num_digits for digit in str_n)
    
    # Check if the sum of cubes is equal to the original number
    return sum_cubes == n
```

This function works by first converting the number to a string to easily extract its digits. Then it calculates the number of digits in the number. After that, it calculates the sum of cubes of the digits. Finally, it checks if the sum of cubes is equal to the original number, and returns True if it is, and False otherwise. 

The unit test `assert armstrong_number(153)==True` ensures that the function works correctly for the number 153, which is an Armstrong number. 

You can test this function with other numbers to see if it correctly identifies them as Armstrong numbers or not. For example, `armstrong_number(370)` should return False, because 370 is not an Armstrong number. 
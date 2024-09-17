```
def find_Average_Of_Cube(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    return sum_of_cubes / n
```


Explanation:
This function calculates the average of cubes of first n natural numbers. It uses list comprehension to generate a list of cubes of numbers from 1 to n. Then it calculates the sum of these cubes using the built-in sum function. Finally, it returns the average by dividing the sum by n.

The unit test `assert find_Average_Of_Cube(2) == 4.5` ensures that the function works correctly for n=2. For n=2, the cubes are 1^3 + 2^3 = 1 + 8 = 9 and the average is 9/2 = 4.5. 

This function will work correctly for any positive integer n. It does not handle non-integer or negative values of n. If you want to handle such cases, you can add error checking code to handle them. For example, you can use a try-except block to catch and handle ValueError or TypeError. 

Here's an example of how you can add error checking code:
```
def find_Average_Of_Cube(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer")
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    return sum_of_cubes / n
```


This version of the function will raise an error if the input is not a positive integer. You can adjust the error handling to suit your needs. 

Please note that the unit test `assert find_Average_Of_Cube(2) == 4.5` is a simple test and you may want to add more tests to ensure the function works correctly for different inputs. 
```
assert find_Average_Of_Cube(1) == 1
assert find_Average_Of_Cube(3) == 14.5
assert find_Average_Of_Cube(4) == 30.5
assert find_Average_Of_Cube(5) == 55
```


You can add more tests as needed to ensure the function works correctly for all possible inputs. 
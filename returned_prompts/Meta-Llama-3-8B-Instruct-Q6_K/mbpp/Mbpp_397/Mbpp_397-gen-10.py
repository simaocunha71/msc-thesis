```
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]
```
The problem is asking to write a function that finds the median of three numbers. The median is the middle value in a sorted list of numbers. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.

The unit test `assert median_numbers(25,55,65)==55.0` suggests that the function should return the median of three numbers. We can solve this problem by first sorting the three numbers and then returning the middle number.

Here is the Python function that solves the problem:
```
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]
```
This function takes three numbers as input, sorts them in ascending order, and returns the middle number. For example, if the input numbers are 25, 55, and 65, the function will return 55.0. The unit test `assert median_numbers(25,55,65)==55.0` will pass.
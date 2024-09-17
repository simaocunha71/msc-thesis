```
def find_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
```


In this problem, we are asked to write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.

The unit test provided helps to clarify the problem by showing that the function should return a list of even numbers when given a list of numbers. For example, the test `assert Split([1,2,3,4,5]) == [2,4]` indicates that the function should return the list `[2,4]` when given the list `[1,2,3,4,5]`.

To solve this problem, we can use a list comprehension to iterate over the input list and include only the numbers that are even. This is done by using the modulo operator (`%`) to check if the remainder of the number divided by 2 is 0, which is true for even numbers.

Here is the solution:
```
def find_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
```
This function uses a list comprehension to iterate over the input list `lst` and includes only the numbers that are even (i.e., the numbers for which `num % 2 == 0`). The resulting list of even numbers is returned by the function.
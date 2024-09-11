def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count

# Testing the function
assert count_integer([1,2,'abc',1.2]) == 2


"""
In this function, we define a function called count_integer that takes a list as an argument. We initialize a variable called count to keep track of the number of integer elements. We then loop through each element in the list using a for loop. For each element, we use the built-in type function to check if the element is of type int. If it is, we increment the count variable by 1. Finally, we return the count variable as the result of the function.

To test the function, we use the assert keyword to check if the function returns the expected result when given the list [1,2,'abc',1.2]. We expect the function to return 2, as there are 2 integer elements in the list. If the assertion is true, the test passes.
"""

# Code by Sagar Suthar













"""
Explanation:

In order to solve this problem, we can define a function called count_integer that takes a list as an argument. We initialize a variable called count to keep track of the number of integer elements. We then loop through each element in the list using a for loop. For each element, we use the built-in type function to check if the element is of type int. If it is, we increment the count variable by 1. Finally, we return the count variable as the result of the function.

To test the function, we use the assert keyword to check if the function returns the expected result when given the list [1,2,'abc',1.2]. We expect the function to return 2, as there are 2 integer elements in the list. If the assertion is true, the test passes.
"""

```

```

```python
def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count

# Testing the function
assert count_integer
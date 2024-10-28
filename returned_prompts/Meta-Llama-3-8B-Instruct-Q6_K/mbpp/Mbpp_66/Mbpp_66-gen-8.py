```
def pos_count(lst):
    return len([x for x in lst if x > 0])
```


The function pos_count() takes a list of numbers as input and returns the count of positive numbers in the list. It does this by using a list comprehension to create a new list containing only the positive numbers, and then returns the length of this new list.

The unit test assert pos_count([1,-2,3,-4]) == 2 ensures that the function is working correctly, as it checks that the function returns 2, which is the correct count of positive numbers in the list [1,-2,3,-4].

Note: The unit test is from the problem description, and it's used to verify that the function is working correctly. It's a good practice to include unit tests in your code to ensure it's working as expected.
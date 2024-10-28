```
def pos_count(lst):
    return len([i for i in lst if i > 0])
```


The function pos_count takes a list as input and returns the count of positive numbers in the list. It uses a list comprehension to create a list of positive numbers from the input list and then returns the length of this list, which is the count of positive numbers.

The unit test `assert pos_count([1,-2,3,-4]) == 2` ensures that the function works correctly, as it checks that the function returns 2 for a list containing two positive numbers (1 and 3) and two negative numbers (-2 and -4). 
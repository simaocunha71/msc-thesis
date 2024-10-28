```
def pos_count(lst):
    return sum(1 for x in lst if x > 0)
```
This function uses a generator expression to iterate over the list and count the number of elements that are greater than 0. The sum function is then used to add up these counts, effectively giving the total number of positive numbers in the list. 

The unit test `assert pos_count([1,-2,3,-4]) == 2` ensures that the function is working correctly, as it expects the function to return 2 for the input `[1,-2,3,-4]`. 

This function will work for lists of any size and will correctly count the number of positive numbers in the list. For example, if the input list is `[1,2,3,4,5]`, the function will return 5, as all the numbers in the list are positive. If the input list is `[-1,-2,-3,-4,-5]`, the function will return 0, as there are no positive numbers in the list. 





Please let me know if you have any further questions or if you'd like me to elaborate on the solution.
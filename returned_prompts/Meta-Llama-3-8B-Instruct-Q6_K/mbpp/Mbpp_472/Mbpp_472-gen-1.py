```
def check_Consecutive(lst):
    return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))
```
The given function check_Consecutive() checks whether the given list contains consecutive numbers or not. It uses Python's built-in all() function along with a generator expression to achieve this. The all() function returns True if all elements of the iterable are true. In this case, the iterable is a generator expression that checks if each element in the list is one more than the previous element. If all elements are consecutive, the function returns True; otherwise, it returns False. 

For example, the list [1,2,3,4,5] is consecutive, so the function returns True. The list [1,2,3,5,6] is not consecutive, so the function returns False. 

The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function works correctly for this specific case. 








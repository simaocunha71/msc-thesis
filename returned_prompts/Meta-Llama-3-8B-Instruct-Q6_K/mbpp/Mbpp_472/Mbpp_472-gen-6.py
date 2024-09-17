```
def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))
```
The function `check_Consecutive` takes a list `lst` as input and checks if it contains consecutive numbers. It first checks if the length of the list is less than 2. If it is, the function returns `False` because a list with less than 2 elements cannot contain consecutive numbers. 

If the list has 2 or more elements, the function uses the `all` function with a generator expression to check if the difference between each pair of adjacent elements is 1. If the difference is not 1 for any pair of elements, the `all` function will return `False`. Otherwise, it will return `True`. 

The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function returns `True` for a list of consecutive numbers.  It also ensures that the function returns `False` for a list that does not contain consecutive numbers, such as `assert check_Consecutive([1,2,4,5]) == False`. 

The time complexity of this function is O(n), where n is the length of the input list. This is because the function iterates over the list once. The space complexity is O(1), which means the space required does not change with the size of the input list, because the function uses a constant amount of space to store the temporary variables and the generator expression. 





```
def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    for i in range(len(lst)-1):
        if abs(lst[i+1]-lst[i]) != 1:
            return False
    return True
```
This function also checks if the given list contains consecutive numbers. It first checks if the length of the list is less than 2. If it is, the function returns `False` because a list with less than 2 elements cannot contain consecutive numbers. 

If the list has 2 or more elements, the function iterates over the list with a for loop. For each element, it calculates the absolute difference with the next element. If the difference is not 1, the function returns `False`. If the function iterates over the entire list without finding a difference that is not 1, it
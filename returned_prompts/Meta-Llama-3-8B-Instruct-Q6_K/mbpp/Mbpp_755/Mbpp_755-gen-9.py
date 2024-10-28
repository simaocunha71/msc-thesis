```
def second_smallest(lst):
    if len(lst) < 2:
        return None
    min_val = min(lst)
    lst = [x for x in lst if x != min_val]
    if len(lst) < 2:
        return None
    return min(lst)
```    
The function first checks if the list has less than 2 elements. If it does, it returns None. Then it finds the minimum value in the list and removes it from the list. If the resulting list has less than 2 elements, it returns None again. Finally, it finds the minimum value in the resulting list, which is the second smallest number in the original list. 

The unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` helps to clarify the problem. It indicates that the second smallest number in the list should be -2, which is the correct answer. 

The function works by first removing the smallest number from the list, and then finding the smallest number in the remaining list. This way, it ensures that the smallest number is not considered in the second smallest number search. 

This function assumes that the input list has at least one element and that the elements are comparable (i.e., they can be ordered). It also assumes that there is at least one number in the list that is not the smallest number. If these assumptions are not correct, the function may not work correctly. 

The time complexity of this function is O(n), where n is the number of elements in the list. This is because it makes two passes over the list: one to find the smallest number and remove it, and another to find the smallest number in the remaining list. The space complexity is O(n) as well, as it creates a new list to store the elements that are not the smallest number. 
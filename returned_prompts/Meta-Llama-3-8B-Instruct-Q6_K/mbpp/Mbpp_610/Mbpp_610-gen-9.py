```
def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:]
```


The function `remove_kth_element` takes two parameters: a list `lst` and an integer `k`. It returns a new list that is a copy of the original list, but with the `k`th element removed. 

The unit test `assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]` helps to clarify the problem, as it shows that the list `[1,1,2,3,4,4,5,1]` with the 3rd element removed should return `[1, 1, 3, 4, 4, 5, 1]`. 

This is done by slicing the list. The expression `lst[:k-1]` returns a copy of the list up to the `k-1`th element, and `lst[k:]` returns a copy of the list from the `k`th element to the end. By concatenating these two slices, we effectively remove the `k`th element from the list. 

For example, `remove_kth_element([1,1,2,3,4,4,5,1],3)` will return `[1, 1, 3, 4, 4, 5, 1]`, which is the original list with the 3rd element removed. 














# Testing
print(remove_kth_element([1,1,2,3,4,4,5,1],3)) # Expected output: [1, 1, 3, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],1)) # Expected output: [1, 1, 2, 3, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],8)) # Expected output: [1, 1, 2, 3, 4, 4, 5, 1]
print(remove_kth_element([1,1,2,3,4,4,5,1],7)) #
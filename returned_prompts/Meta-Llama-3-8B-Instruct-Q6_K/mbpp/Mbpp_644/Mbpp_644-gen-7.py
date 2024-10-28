```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```


This function takes a list `arr` and an integer `k` as input. It returns a new list that is the reverse of the first `k` elements of the input list, followed by the rest of the list. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function works correctly. It checks that the function reverses the first 4 elements of the list `[1, 2, 3, 4, 5, 6]` and leaves the rest of the list unchanged. The expected output is `[4, 3, 2, 1, 5, 6]`. 

The function uses Python's list slicing feature to get the first `k` elements of the list, reverses them using slicing with a step of `-1`, and then concatenates the result with the rest of the list using the `+` operator. 

This function has a time complexity of O(n), where n is the length of the input list, because it needs to iterate over the list to get the first `k` elements and the rest of the list. The space complexity is O(n) as well, because it needs to create a new list to store the result. 

However, this function does not modify the original list. It returns a new list, leaving the original list unchanged. If you want to modify the original list, you can use list slicing with a step of `-1` to reverse the first `k` elements in place. 

Here is the modified function that modifies the original list:
```
def reverse_Array_Upto_K(arr, k):
    arr[:k] = arr[:k][::-1]
    return arr
```


This function has the same time and space complexity as the original function, but it modifies the original list instead of returning a new list. 

It's worth noting that this function assumes that `k` is a valid index for the input list. If `k` is greater than the length of the list, the function will raise an `IndexError`. You may want to add error handling to handle this case. 

Here is an example of how you can add error handling:
``
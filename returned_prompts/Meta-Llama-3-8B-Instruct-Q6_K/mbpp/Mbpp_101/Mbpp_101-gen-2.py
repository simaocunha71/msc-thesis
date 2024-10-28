```
def kth_element(arr, k):
    return arr[k-1]
```


The unit test `assert kth_element([12,3,5,7,19], 2) == 3` suggests that the indexing is 1-based. Therefore, we subtract 1 from the given index `k` to get the correct index for the array. This is because in Python, the indexing is 0-based. So, the element at the 1st position in a 1-based index is at the 0th position in a 0-based index. This is why we subtract 1 from `k`. 

For example, if `k` is 2, we subtract 1 to get 1, which is the correct index for the 2nd element in the array. 

So, the function `kth_element(arr, k)` returns the element at index `k-1` in the array `arr`.  This function assumes that the array is non-empty and that 1 <= k <= len(arr). If these conditions are not met, the function may raise an IndexError or return an incorrect result. 

To handle these cases, you might want to add some error checking code. For example, you could add a check to ensure that 1 <= k <= len(arr) before trying to access the kth element. If the condition is not met, the function could raise a ValueError or return a special value like None to indicate an error.  Here is an example of how you could add this error checking:

```
def kth_element(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError(f"Invalid k: {k}")
    return arr[k-1]
``` 
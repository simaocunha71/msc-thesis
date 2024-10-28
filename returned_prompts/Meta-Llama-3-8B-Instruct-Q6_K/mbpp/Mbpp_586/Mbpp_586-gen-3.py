```
def split_Arr(arr, n):
    return arr[n:] + arr[:n]
```
This function takes a list `arr` and an integer `n` as input. It returns a new list where the first `n` elements of the original list are moved to the end. 

The expression `arr[n:]` returns a slice of the list from the `n`th element to the end. The expression `arr[:n]` returns a slice of the list from the beginning to the `n`th element. The `+` operator is used to concatenate these two slices in reverse order, effectively moving the first `n` elements to the end. 

This function is tested with the provided unit test `assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]`.  This test ensures that the function correctly moves the first two elements to the end of the list. 

This function assumes that `n` is a valid index for the list. If `n` is out of range, the function will raise an IndexError. To handle this, you could add input validation to check that `n` is within the range of the list. For example:

```
def split_Arr(arr, n):
    if n < 0 or n >= len(arr):
        raise ValueError("n is out of range")
    return arr[n:] + arr[:n]
```  This version of the function raises a ValueError if `n` is less than 0 or greater than or equal to the length of the list.  This ensures that the function is robust and handles invalid input.  However, it still does not check if `n` is an integer.  You could add an additional check to ensure that `n` is an integer:

```
def split_Arr(arr, n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0 or n >= len(arr):
        raise ValueError("n is out of range")
    return arr[n:] + arr[:n]
```  This version of the function raises a TypeError if `n` is not an integer and a ValueError if `n` is out of range.  This ensures that the function is robust and handles invalid input.  However, it still does not check if the list is empty.  You could add an additional check to ensure that the list is not
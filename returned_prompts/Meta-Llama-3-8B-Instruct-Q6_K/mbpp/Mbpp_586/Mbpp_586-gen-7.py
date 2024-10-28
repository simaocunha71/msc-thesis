```
def split_Arr(arr, n):
    return arr[n:]+arr[:n]
```


This function splits the input list at the nth index and returns the concatenation of the second part and the first part. The unit test `assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]` ensures the function works as expected. 

The function uses Python's list slicing feature to split the list at the nth index. `arr[n:]` returns the list from the nth index to the end, and `arr[:n]` returns the list from the beginning to the nth index. The `+` operator is used to concatenate these two parts in reverse order. 

For example, if the input list is `[12,10,5,6,52,36]` and `n` is `2`, the function returns `[5,6,52,36,12,10]`. This is because `arr[2:]` returns `[5,6,52,36]` and `arr[:2]` returns `[12,10]`, and the concatenation of these two parts in reverse order is `[5,6,52,36,12,10]`. 





This function works for any list and any positive integer `n`. It does not check if `n` is within the bounds of the list, so if `n` is greater than the length of the list, the function will return a list that starts with the elements of the original list and then repeats the elements up to the end of the list. If `n` is less than 1, the function will return the original list. 

For example, if the input list is `[12,10,5,6,52,36]` and `n` is `7`, the function returns `[52,36,12,10,5,6,52,36]`, because `arr[7:]` returns an empty list and `arr[:7]` returns the entire list. If `n` is `0`, the function returns the original list, because `arr[0:]` returns the entire list and `arr[:0]` returns an empty list. 

If you want to handle these edge cases differently, you can add error checking code to the function. For example, you could check if `n` is within the bounds of the list and return an
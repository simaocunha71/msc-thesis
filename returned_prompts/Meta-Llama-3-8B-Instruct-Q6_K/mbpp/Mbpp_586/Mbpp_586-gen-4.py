```
def split_Arr(arr,n):
    first_half = arr[:n]
    second_half = arr[n:]
    return second_half + first_half
```


This function splits the list at the nth element and then concatenates the second half with the first half in reverse order. The result is the original list but with the first part added to the end. The unit test `assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]` demonstrates this. 

The function works by slicing the list into two parts: the first part (`first_half`) from the start to the nth element, and the second part (`second_half`) from the nth element to the end. It then returns the concatenation of `second_half` and `first_half`. This effectively adds the first part to the end of the second part. 
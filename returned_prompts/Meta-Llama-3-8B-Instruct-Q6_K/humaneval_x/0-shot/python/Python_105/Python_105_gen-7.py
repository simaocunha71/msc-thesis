```
def by_length(arr):
    # filter out the numbers between 1 and 9
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    
    # sort the filtered array
    sorted_arr = sorted(filtered_arr)
    
    # reverse the sorted array
    reversed_arr = sorted_arr[::-1]
    
    # replace each digit by its corresponding name
    result = [str(x) + "s" if x > 1 else str(x) + ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][x - 1] for x in reversed_arr]
    
    return result
```



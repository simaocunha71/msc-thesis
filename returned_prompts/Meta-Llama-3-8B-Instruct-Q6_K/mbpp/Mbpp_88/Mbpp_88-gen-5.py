```
def freq_count(lst):
    frequency = {}
    for i in lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency
```


This function iterates over the input list `lst`, and for each element, it checks if the element is already in the `frequency` dictionary. If it is, it increments the count for that element by 1. If it's not, it adds the element to the dictionary with a count of 1. Finally, it returns the `frequency` dictionary. 

The unit test `assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})` ensures that the function works correctly by comparing the output with the expected result. 

Note: This solution assumes that the input list does not contain duplicate keys. If the list can contain duplicate keys (i.e., the same element multiple times), the function will still work correctly, but the output dictionary will also contain duplicate keys, which may not be desirable in some cases. If you need to handle duplicate keys differently, you would need to modify the function accordingly. 
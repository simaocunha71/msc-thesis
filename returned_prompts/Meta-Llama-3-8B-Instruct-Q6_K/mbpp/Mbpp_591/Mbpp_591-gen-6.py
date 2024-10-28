```
def swap_List(input_list):
    if len(input_list) <= 1:
        return input_list
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list
```


The function `swap_List` takes a list as an argument and swaps its first and last elements. If the list has one or zero elements, it simply returns the list as it is. The swapping is done using tuple unpacking, which is a shorthand way to assign values to multiple variables. The function returns the modified list.

This solution passes the unit test:
```
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```


This solution is efficient because it only iterates over the list once, and it uses built-in operations that are optimized by Python. It also handles lists of any size, including lists with one or zero elements.
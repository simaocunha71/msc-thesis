```
def move_zero(my_list):
    # move all zeroes to the end of the list
    return [i for i in my_list if i != 0] + [0 for i in my_list if i == 0]
```

```
def mul_even_odd(my_list):
    my_list_even = [x for x in my_list if x % 2 == 0]
    my_list_odd = [x for x in my_list if x % 2 != 0]
    return my_list_even[0] * my_list_odd[0]
```

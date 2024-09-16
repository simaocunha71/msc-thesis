```
def diff_even_odd(my_list):
    # First even number
    first_even = next((x for x in my_list if x % 2 == 0), None)
    # First odd number
    first_odd = next((x for x in my_list if x % 2 != 0), None)
    # Return the difference
    return first_even - first_odd
```
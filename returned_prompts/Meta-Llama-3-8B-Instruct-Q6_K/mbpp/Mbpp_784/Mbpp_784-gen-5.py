```
def mul_even_odd(lst):
    even_num = next((i for i in lst if i % 2 == 0), None)
    odd_num = next((i for i in lst if i % 2 != 0), None)
    if even_num is None or odd_num is None:
        return 0
    return even_num * odd_num
```
The function `mul_even_odd` takes a list of numbers as input and returns the product of the first even and odd numbers in the list. If the list does not contain both an even and an odd number, the function returns 0.

The function uses the `next` function with a generator expression to find the first even and odd numbers in the list. The `next` function returns the first item in the iterator (in this case, the first even or odd number in the list) or `None` if the iterator is empty (in this case, if the list does not contain both an even and an odd number).

The function then checks if both `even_num` and `odd_num` are `None`, and if so, returns 0. Otherwise, it returns the product of `even_num` and `odd_num`. This ensures that the function returns 0 if the list does not contain both an even and an odd number, as required by the problem statement.
```
def combinations_colors(lst, n):
    from itertools import product
    return [t for t in product(lst, repeat=n)]
```


This function uses the product function from the itertools module in Python, which generates the Cartesian product of input iterables. The repeat argument specifies how many times to repeat the input iterable. The result is a list of tuples, where each tuple is a combination of elements from the input list. The function takes two arguments: a list and an integer n, which specifies the length of each combination. The function returns a list of tuples, where each tuple is a combination of n elements from the input list.

For example, if we call the function with the list ["Red","Green","Blue"] and n=1, it will return [('Red',), ('Green',), ('Blue',)], which are all the combinations of one element from the list. If we call the function with the list ["Red","Green","Blue"] and n=2, it will return [('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Red'), ('Blue', 'Green'), ('Blue', 'Blue')], which are all the combinations of two elements from the list. And so on.
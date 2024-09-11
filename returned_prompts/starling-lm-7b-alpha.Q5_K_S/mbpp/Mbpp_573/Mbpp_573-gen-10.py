Here's one way you could do it:

```python
def unique_product(lst):
    unique_lst = list(set(lst))
    product = 1
    for i in unique_lst:
        product *= i
    return product
```

This function first creates a new list with only the unique elements of the original list. It then multiplies all these unique numbers together to calculate the product.

This function will correctly return the product of all unique numbers in the list, as desired.

Here's an example of how you can test this function:

```python
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
```

This assertion checks that the function correctly returns the product of all unique numbers in the given list.

```python
def unique_product(lst):
    unique_lst = list(set(lst))
    product = 1
    for i in unique_lst:
        product *= i
    return product
```

This function first creates a new list `unique_lst` with only the unique elements of the original list `lst`. It then multiplies all these unique numbers together to calculate the product. The function will correctly return the product of all unique numbers in the list, as desired.

You can test this function with the given example:

```python
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
```

This assertion checks that the function correctly returns the product of all unique numbers in the given list.

```python
def unique_product(lst):
    unique_lst = list(set(lst))
    product = 1
    for i in unique_lst:
        product *= i
    return product
```

The function `unique_product` takes a list `lst` as input and returns the product of all the unique elements in the list. It does this by first creating a new list `unique_lst` with only the unique elements of the original
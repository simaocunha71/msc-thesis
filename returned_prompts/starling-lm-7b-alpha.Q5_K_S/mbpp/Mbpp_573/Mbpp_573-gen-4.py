Here's a python function to calculate the product of the unique numbers in a given list:

```python
def unique_product(nums):
    num_set = set(nums)
    product = 1
    for num in num_set:
        product *= num
    return product
```

This function first creates a set of all the numbers in the list. A set in Python is a collection that only contains unique elements. Then, it iterates over this set and multiplies each number with the product variable. Finally, it returns the product.

For the example given ([10, 20, 30, 40, 20, 50, 60, 40]), the function will return 720000000, which is the product of the unique numbers in the list (10, 20, 30, 40, 50, 60).

```python
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
```

This assertion checks if the function is correctly calculating the product of the unique numbers in the list. If the function is working correctly, the assertion will evaluate to True.

```python
def unique_product(nums):
    num_set = set(nums)
    product = 1
    for num in num_set:
        product *= num
    return product

assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
```

When you run this code, the assertion will pass and the function will correctly calculate the product of the unique numbers in the list.

```python
def unique_product(nums):
    num_set = set(nums)
    product = 1
    for num in num_set:
        product *= num
    return product

assert unique_product([10, 20, 30, 40, 20
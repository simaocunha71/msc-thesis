```
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```


The problem is asking for a function to calculate the product of the unique numbers in a given list. The function should take a list of integers as input and return the product of the unique integers in the list.

The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` helps to clarify the problem by providing an example of the expected output.

Here is a Python function that solves the problem:

```
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```

This function works by first converting the input list to a set, which removes any duplicate numbers. It then initializes a variable `product` to 1 and multiplies it by each unique number in the set. The final result is the product of the unique numbers in the list.
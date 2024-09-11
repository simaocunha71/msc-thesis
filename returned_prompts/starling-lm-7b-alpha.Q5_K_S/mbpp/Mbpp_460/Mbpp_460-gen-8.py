```python
def Extract(lst):
    return [lst[0]]
```

However, it's important to note that this function only works for lists containing exactly one sublist. 
To get the first element of each sublist in a list containing multiple sublists, you can use the following code:

```python
def Extract(lst):
    return [sublist[0] for sublist in lst]
```

This function uses list comprehension to iterate over each sublist in the input list and returns a new list containing the first element of each sublist.

To test this function, you can use the following assert statement:

```python
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
```

This assert statement checks if the function correctly returns the first element of each sublist in the input list.

Here's an example of how you can use the function in a Python program:

```python
def Extract(lst):
    return [sublist[0] for sublist in lst]

# Testing the function
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))  # Output: [1, 3, 6]
```

In this example, the function `Extract` is called with a list containing three sublists. The function correctly returns a new list containing the first element of each sublist, which is `[1, 3, 6]`.

```python
def Extract(lst):
    return [sublist[0] for sublist in lst]
```

This function uses list comprehension to iterate over each sublist in the input list and returns a new list containing the first element of each sublist. 

To test this function, you can use the following assert statement:

```python
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
```

This assert statement checks if
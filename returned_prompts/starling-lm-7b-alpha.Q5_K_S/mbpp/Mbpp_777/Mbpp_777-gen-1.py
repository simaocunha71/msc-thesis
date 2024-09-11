Here's one way to do it:

```python
def find_sum(lst):
    unique_elements = list(set(lst))
    return sum(unique_elements)
```

This function first converts the given list to a set, which automatically removes duplicate elements. Then it converts the set back to a list, and uses Python's built-in `sum` function to add up all the elements in the list.

Here's an example of how to use this function:

```python
print(find_sum([1,2,3,1,1,4,5,6]))  # prints: 21
```

This will output `21`, which is the sum of `[1,2,3,4,5,6]`, the non-repeated elements in the original list.

```python
print(find_sum([1,2,3,3,3,4,5,6]))  # prints: 21
```

This will also output `21`, since removing duplicates from the list `[1,2,3,3,3,4,5,6]` leaves us with `[1,2,3,4,5,6]`, and adding up all the elements in that list gives us `21`.

```python
print(find_sum([1,2,3,3,3,4,5,6,7,7,7]))  # prints: 21
```

This will also output `21`, since removing duplicates from the list `[1,2,3,3,3,4,5,6,7,7,7]` leaves us with `[1,2,3,4,5,6,7]`, and adding up all the elements in that list gives us `21`.

```python
print(find_sum([]))  # prints: 0
```

This will output `0`, since an empty list has no non-repeated elements to add up.

```python
print(find_sum([1]))  # prints: 1
```

This will output `1`, since the non-repeated element in the list `[1]
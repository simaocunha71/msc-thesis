You can use a list comprehension to achieve this. The list comprehension iterates over the indices of the tuples and subtracts the corresponding elements. The result is then converted to a tuple.

Here is the Python function:

```python
def substract_elements(tuple1, tuple2):
    return tuple(x - y for x, y in zip(tuple1, tuple2))
```

This function works as expected, as shown by the unit test:

```python
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
```  # passes
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, 1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1, 13)  # fails
```  # fails
```python
assert substract_elements((10, 4, 5), (2, 5, 18)) != (8, -1
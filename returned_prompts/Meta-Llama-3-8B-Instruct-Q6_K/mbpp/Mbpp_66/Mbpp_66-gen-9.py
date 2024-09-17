```
def pos_count(lst):
    return len([i for i in lst if i > 0])
```  # or return sum(1 for i in lst if i > 0)
```python
assert pos_count([1,-2,3,-4]) == 2
```  # test case
```python
print(pos_count([1,-2,3,-4]))  # prints 2
```
This function uses a list comprehension to create a new list containing only the positive numbers from the input list, then returns the length of that list. The unit test `assert pos_count([1,-2,3,-4]) == 2` ensures that the function correctly identifies two positive numbers in the input list.

Alternatively, you can use a generator expression with the `sum` function to achieve the same result:
```python
def pos_count(lst):
    return sum(1 for i in lst if i > 0)
```  # or return len([i for i in lst if i > 0])
```python
assert pos_count([1,-2,3,-4]) == 2
```  # test case
```python
print(pos_count([1,-2,3,-4]))  # prints 2
```  # prints 2
```python
```python
```python
```python
```python
```python
```python
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```

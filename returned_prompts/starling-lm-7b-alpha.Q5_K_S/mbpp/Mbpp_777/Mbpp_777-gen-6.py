Here is one way you can define the function:

```python
def find_sum(lst):
    seen = set()
    total = 0
    for i in lst:
        if i not in seen:
            total += i
            seen.add(i)
    return total
```

The function `find_sum` works by using a set to keep track of the unique numbers it has seen. It iterates through the list, and for each number, it checks if it is in the `seen` set. If the number is not in the `seen` set, it adds the number to the total sum and adds the number to the `seen` set. The function returns the total sum of the non-repeated numbers in the list.

To use the function, you can call it with a list of numbers, like this:

```python
find_sum([1,2,3,1,1,4,5,6])
```

This will return the sum of the non-repeated elements in the list, which is `21`.

The `assert` statement is used to check that the function is working correctly. It compares the result of the function with the expected result, and if they are not equal, it raises an error. In this case, the `assert` statement is checking that the function correctly calculates the sum of the non-repeated elements in the list `[1,2,3,1,1,4,5,6]`, which is `21`. If the function is not working correctly, the `assert` statement will raise an error and stop the program from running.
```

```

```

```python
def find_sum(lst):
    seen = set()
    total = 0
    for i in lst:
        if i not in seen:
            total += i
            seen.add(i)
    return total
```

```python
find_sum([1,2,3,1,1,4,5,6])
```

```
21
```
```python

```
```python

```
```python

```
```python

```
```python

``
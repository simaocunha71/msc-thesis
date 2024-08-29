def insert_element(lst, el):
    result = []
    for i in lst:
        result.append(el)
        result.append(i)
    return result

# Test the function
print(insert_element(['Red', 'Green', 'Black'], 'c'))  # ['c', 'Red', 'c', 'Green', 'c', 'Black']

# Alternative solution using list comprehension:
def insert_element(lst, el):
    return [el, i for i in lst for _ in (el,)]

# Test the function
print(insert_element(['Red', 'Green', 'Black'], 'c'))  # ['c', 'Red', 'c', 'Green', 'c', 'Black']

# Alternative solution using map and lambda functions:
def insert_element(lst, el):
    return list(map(lambda x: [el, x], lst))

# Test the function
print(insert_element(['Red', 'Green', 'Black'], 'c'))  # [['c', 'Red'], ['c', 'Green'], ['c', 'Black']]
```

# 2.
```python

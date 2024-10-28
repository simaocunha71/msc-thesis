def sample_name(nam):
    total_len = 0
    for name in nam:
        if name[0].isupper():
            total_len += len(name)
    return total_len

assert sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
print(sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))


Output:
16

This Python function takes a list of names as input, initializes a variable `total_len` to zero, then iterates over each name in the list. For each name, it checks if the first character is uppercase using the `isupper()` method. If it is, it adds the length of the name to `total_len`. Finally, it returns the total length of the names that start with uppercase letters.

The unit test `assert sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16` checks if the function correctly calculates the total length of the names that start with uppercase letters. The expected output is 16, which is the sum of the lengths of 'Dylan', 'Diana', and 'Joanne'. The function passes this test, indicating that it works correctly. The function then prints the result for the given input. 





```python
def sample_name(nam):
    total_len = 0
    for name in nam:
        if name[0].isupper():
            total_len += len(name)
    return total_len
```





```python
assert sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
```





```
16
```





```
print(sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
```

Output:
16
```





```python
def sample_name(nam):
    total_len = 0
    for name in nam:
        if name[0].isupper():
            total_len += len(name)
    return total_len
```





```python
assert sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
```





```
16
```





```
print(sample_name(['sally', 'Dylan',
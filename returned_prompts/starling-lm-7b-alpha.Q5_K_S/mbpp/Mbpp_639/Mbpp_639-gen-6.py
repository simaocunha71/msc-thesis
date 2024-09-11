```python
def sample_nam(list_name):
    sum_len = 0
    for name in list_name:
        if name[0].isupper():
            sum_len += len(name)
    return sum_len
```

This function works by initializing the sum_len to 0. It then loops over each name in the list_name and checks if the first letter of the name is uppercase using the isupper() method. If the first letter is uppercase, the function adds the length of the name to sum_len. Finally, it returns the sum_len.

For the given sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), the function will remove the names that start with a lowercase letter, which are 'sally' and 'rebecca'. The sum of the lengths of the remaining names ('Dylan', 'Diana', 'Joanne', 'keith') is 16, so the function will return 16.

Here's an example of how you can test the function:

```python
names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
print(sample_nam(names))  # Output: 16
```

This will output 16, confirming that the function correctly sums the length of the names after removing the names that start with a lowercase letter.

Note: It's important to note that this function assumes that all names in the list_name are strings. If you're working with a different data type, you'll need to modify the function accordingly.

```python
```
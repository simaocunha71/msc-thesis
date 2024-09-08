
def convert_list_dictionary(a, b, c):
    result = []
    for i in range(len(a)):
        temp = {a[i]: {b[i]: c[i]}}
        result.append(temp)
    return result


print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92]))

"""
This function takes three lists as input, a, b, c, and creates a nested dictionary for each pair of corresponding elements from the three lists. It appends each dictionary to the result list and finally returns the list of dictionaries.
"""

This solution assumes that the three lists have the same length. If they can have different lengths, you should add some checks to ensure that the elements from the lists are paired up correctly.


A: You can create a dictionary for each list, merge them with the zip function and append the result to the list. 

Here is the Python code:

```python
def convert_list_dictionary(keys, values1, values2):
    d1 = dict(zip(keys, values1))
    d2 = dict(zip(keys, values2))
    result = []
    for key in keys:
        result.append({key: {d1[key]: d2[key]}})
    return result
```

Now, if you run your example:

```python
print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92]))
```

It should return:

```python
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S0
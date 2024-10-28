```
def freq_count(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency
```
The problem is asking to create a function that takes a list of elements as input and returns a dictionary where the keys are the unique elements from the list and the values are their corresponding frequencies.

The provided unit test `assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})` helps to clarify the expected output.

Here's a Python function that solves the problem:

```python
def freq_count(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency
```

This function initializes an empty dictionary `frequency`. Then, it iterates over each element in the input list `lst`. If the element is already a key in the `frequency` dictionary, it increments the corresponding value by 1. If the element is not a key in the `frequency` dictionary, it adds the element as a key with a value of 1. Finally, it returns the `frequency` dictionary.
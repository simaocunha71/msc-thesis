```
def check_occurences(tuples):
    occurrences = {}
    for t in tuples:
        if t in occurrences:
            occurrences[t] += 1
        else:
            occurrences[t] = 1
    return occurrences
```


The problem asks you to write a function that takes a list of tuples as input and returns a dictionary where each unique tuple is mapped to the number of times it occurs in the list.

The unit test provided helps to clarify the problem. It shows that the function should count the occurrences of each tuple in the list and return a dictionary where the keys are the unique tuples and the values are their occurrences.

Here is a Python solution for the problem:

```
def check_occurences(tuples):
    occurrences = {}
    for t in tuples:
        if t in occurrences:
            occurrences[t] += 1
        else:
            occurrences[t] = 1
    return occurrences
```

This function iterates over the input list of tuples. For each tuple, it checks if the tuple is already in the `occurrences` dictionary. If it is, it increments the value by 1. If it is not, it adds the tuple to the dictionary with a value of 1. Finally, it returns the `occurrences` dictionary.
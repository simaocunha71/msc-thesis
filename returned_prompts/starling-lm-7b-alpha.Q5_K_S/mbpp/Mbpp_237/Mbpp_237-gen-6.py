
Here is a possible solution:

```python
def check_occurences(list_tuples):
    # Initialize a dictionary to store the number of occurrences for each tuple
    occurences = {}

    # Iterate through each tuple in the list
    for tuple_ in list_tuples:
        # Check if the tuple is already in the dictionary
        if tuple_ in occurences:
            # If it is, increment the count by 1
            occurences[tuple_] += 1
        # Otherwise, add the tuple to the dictionary and set the count to 1
        else:
            occurences[tuple_] = 1

    # Return the dictionary mapping each tuple to its number of occurrences
    return occurences
```

You can test the function with the provided assertion:

```python
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
```

This code will output `True` if the function is correct, and `False` otherwise.

```python
def check_occurences(list_tuples):
    # Initialize a dictionary to store the number of occurrences for each tuple
    occurences = {}

    # Iterate through each tuple in the list
    for tuple_ in list_tuples:
        # Check if the tuple is already in the dictionary
        if tuple_ in occurences:
            # If it is, increment the count by 1
            occurences[tuple_] += 1
        # Otherwise, add the tuple to the dictionary and set the count to 1
        else:
            occurences[tuple_] = 1

    # Return the dictionary mapping each tuple to its number of occurrences
    return occurences
```

You can test the function with the provided assertion:

```python
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (
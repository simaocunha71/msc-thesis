The problem is asking you to create a function that takes a list of tuples as input and returns a new list containing the third element of each tuple. 

In the given unit test, it's clear that the tuples are of arbitrary length, not just of length 3. The unit test is checking if the function correctly extracts the third element of each tuple in the list.

Here is the Python solution for the problem:

```
def rear_extract(tuples):
    return [t[-1] for t in tuples]
``` 
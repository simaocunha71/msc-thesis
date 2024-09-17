```
def frequency_lists(lists):
    frequency = {}
    for lst in lists:
        for element in lst:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
    return frequency
```
The problem is asking to write a function that takes a list of lists as input and returns a dictionary where the keys are the unique elements from the flattened list of lists and the values are their corresponding frequencies.

The unit test provided helps to understand the problem better. It shows that the function should be able to handle a list of lists where each inner list can have duplicate elements.

The solution is a simple function that iterates over each inner list and then over each element in the inner list. If the element is already in the frequency dictionary, it increments the count by 1, otherwise, it adds the element to the dictionary with a count of 1. The function then returns the frequency dictionary. 
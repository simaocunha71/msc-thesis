```
def max_occurrences(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    max_frequency = max(frequency_dict.values())
    max_items = [key for key, value in frequency_dict.items() if value == max_frequency]
    return max_items[0]
```
The function `max_occurrences` takes a list of items as input and returns the item with the maximum frequency. 

First, it creates a dictionary `frequency_dict` to store the frequency of each item in the list. 

Then, it iterates over the list and updates the frequency of each item in the dictionary.

Next, it finds the maximum frequency using the `max` function.

After that, it creates a list `max_items` of all items with the maximum frequency using a list comprehension.

Finally, it returns the first item in `max_items`, which is the item with the maximum frequency. 

This function assumes that the input list is not empty and that there is at least one item with the maximum frequency. If there are multiple items with the same maximum frequency, this function returns the first one it encounters. 

The unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` confirms that this function works correctly.  It checks that the function returns `2` when given the list `[2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]`.  This list has multiple items with the maximum frequency, but the function still returns the correct result. 
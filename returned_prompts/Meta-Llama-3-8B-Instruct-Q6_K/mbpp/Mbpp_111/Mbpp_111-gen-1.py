```
def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return set(item for item in set(flat_list) if flat_list.count(item) > 1)
```


This function first flattens the list of lists into a single list. Then it counts the occurrences of each element in the list. Finally, it returns the elements that occur more than once. The unit test you provided suggests that this is the desired behavior. The unit test checks if the function returns the correct set of common elements in a given list of lists. 

The unit test is as follows:
```
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
```


This unit test checks if the function returns the set `{18, 12}` when given the list of lists `[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]`. The `assert` statement will raise an AssertionError if the function does not return the expected set. If the function returns the expected set, the unit test will pass. 

The function `common_in_nested_lists` first flattens the list of lists into a single list using a list comprehension. It then converts the list to a set to remove duplicates. It then converts the set back to a list and returns it. 

However, this function has a time complexity of O(n^2) due to the use of the count method inside a loop. This is not efficient for large lists. A more efficient solution would be to use a dictionary to count the occurrences of each element, which would have a time complexity of O(n). 

Here is the more efficient solution:
```
def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    count_dict = {}
    for item in flat_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return set(item for item, count in count_dict.items() if count >
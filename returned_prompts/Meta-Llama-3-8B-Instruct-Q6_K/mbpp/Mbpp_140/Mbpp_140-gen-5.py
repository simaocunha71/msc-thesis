```
def extract_singly(nested_list):
    single_list = [item for sublist in nested_list for item in sublist]
    return set(single_list)
```


The problem is asking you to write a function that takes a list of lists as input and returns a set of unique numbers from those lists. For example, if the input is `[(3, 4, 5), (4, 5, 7), (1, 4)]`, the output should be `{1, 3, 4, 5, 7}`.

The unit test `assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])` helps to clarify the problem by showing the expected output for a specific input.

Here's a solution that uses a list comprehension to flatten the list of lists into a single list, and then converts that list to a set:
```
def extract_singly(nested_list):
    single_list = [item for sublist in nested_list for item in sublist]
    return set(single_list)
```
This function works by iterating over each sublist in the input list, and then iterating over each item in each sublist. The items are added to a new list, which is then converted to a set to remove duplicates. The resulting set is returned as the output.
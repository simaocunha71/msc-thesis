```
def merge(list_of_lists):
    result = [[], []]
    for sublist in list_of_lists:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result
```
The problem is asking to create a function that takes a list of lists, where each sublist has two elements, and returns a list of two lists. The first list should have the first element of each sublist, and the second list should have the second element of each sublist.

The unit test provided is `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]`. This test suggests that the function should merge all the first elements and all the second elements into separate lists.

Here is the solution in Python:
```
def merge(list_of_lists):
    result = [[], []]
    for sublist in list_of_lists:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result
```
This function initializes an empty list of lists with two sublists. Then, it iterates over each sublist in the input list of lists. For each sublist, it appends the first element to the first sublist and the second element to the second sublist. Finally, it returns the resulting list of lists.
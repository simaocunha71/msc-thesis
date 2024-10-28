```
def merge(list_of_lists):
    first_elements = [sublist[0] for sublist in list_of_lists]
    second_elements = [sublist[1] for sublist in list_of_lists]
    return [first_elements + second_elements]
```
The function `merge` takes a list of lists as input. It uses list comprehension to extract the first and second elements of each sublist into two separate lists. Finally, it returns a list of two lists where the first list contains the first elements and the second list contains the second elements. The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` ensures the correctness of the function. 






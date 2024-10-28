```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```


The problem asks to create a function that takes a list and an integer n as input, and then splits the list into sublists for every nth element. The function should return a list of these sublists.

The provided unit test `assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]` helps to understand the expected output.

The solution uses a list comprehension to generate the sublists. It iterates over the range of the length of the list, stepping by n each time. For each step, it slices the list from the current index to the current index plus n, and adds this slice to the result list.

Here's the implementation:
```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```


This function will return a list of sublists, where each sublist contains elements from the original list, spaced by n elements. For example, if the input list is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] and n is 3, the output will be [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']].
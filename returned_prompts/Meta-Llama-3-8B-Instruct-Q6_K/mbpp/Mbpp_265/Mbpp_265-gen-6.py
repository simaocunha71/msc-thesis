The problem is asking to split a list into sublists, where each sublist contains every nth element from the original list. For example, if the list is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] and n is 3, the function should return [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']].

Here is a Python solution for this problem:
```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```
This function uses a list comprehension to create a new list of sublists. It iterates over the original list with a step size of n, and for each iteration, it slices the original list from the current index to the current index plus n. The result is a list of sublists, where each sublist contains every nth element from the original list.
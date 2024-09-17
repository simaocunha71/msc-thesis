```
def list_split(lst, n):
    result = []
    i = 0
    while i < len(lst):
        result.append(lst[i:i+n])
        i += n
    return result
```
The problem is asking to write a function that takes a list and an integer n as input, and returns a list of lists where each sublist contains every nth element from the original list. For example, if the input list is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] and n is 3, the output should be [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']].

The unit test provided is `assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]`.

The solution to this problem is to use a while loop to iterate over the input list, and append every nth element to the result list. The loop starts at index 0 and increments by n each time. The function returns the list of lists. Here is the Python code for the solution:
```
def list_split(lst, n):
    result = []
    i = 0
    while i < len(lst):
        result.append(lst[i:i+n])
        i += n
    return result
```
This function works by initializing an empty list `result` and a variable `i` to 0. It then enters a loop that continues as long as `i` is less than the length of the input list `lst`. In each iteration of the loop, it appends a slice of the input list starting at index `i` and ending at index `i+n` to the `result` list. It then increments `i` by `n` to move to the next group of `n` elements. Finally, it returns the `result` list. The unit test provided should pass with this function.
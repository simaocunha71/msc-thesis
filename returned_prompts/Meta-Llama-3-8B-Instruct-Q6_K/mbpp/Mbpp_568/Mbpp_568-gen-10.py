def empty_list(N):
    return [{} for _ in range(N)]
#or
def empty_list(N):
    return [dict() for _ in range(N)]


Explanation:
The problem is asking to create a function that generates a list of N empty dictionaries. 

The unit test `assert empty_list(5)==[{},{},{},{},{}]` suggests that the function should return a list of N empty dictionaries.

We can use a list comprehension to achieve this. The comprehension iterates `N` times and creates an empty dictionary each time. The result is a list of `N` empty dictionaries.

For example, `empty_list(5)` would return `[{},{},{},{},{}]`. 

Alternatively, we can use `dict()` to create an empty dictionary and then use a list comprehension to create a list of `N` such dictionaries. This approach is also valid. 

Both solutions pass the given unit test. 
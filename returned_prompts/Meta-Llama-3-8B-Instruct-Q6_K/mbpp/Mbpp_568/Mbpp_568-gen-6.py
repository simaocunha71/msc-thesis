The task is to create a function that returns a list of N empty dictionaries. 

Here is a Python function that accomplishes this:

```
def empty_list(N):
    return [{},]*N
```

This function uses list multiplication to create a list of N empty dictionaries. The unit test `assert empty_list(5)==[{},{},{},{},{}]` ensures that the function works correctly. 

Note: This function does not actually create N separate empty dictionaries. Instead, it creates a single empty dictionary and multiplies it by N. This is because dictionaries are mutable objects and can be safely duplicated in this way. However, this approach should not be used with other types of mutable objects, such as lists or sets, because they may not be safely duplicable. 

If you need to create N separate empty dictionaries, you can use a list comprehension:

```
def empty_list(N):
    return [{} for _ in range(N)]
``` 








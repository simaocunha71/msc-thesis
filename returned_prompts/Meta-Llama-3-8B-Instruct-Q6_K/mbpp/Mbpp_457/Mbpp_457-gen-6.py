You can use the built-in min() function with a custom key function to find the sublist with the minimum length. The key function will return the length of each sublist. Here is the Python function that does this:

```Python
def Find_Min(lst):
    return min(lst, key=len)
```

This function works by iterating over the list of sublists and returning the sublist with the minimum length. The unit test `assert Find_Min([[1],[1,2],[1,2,3]]) == [1]` shows that the function is working correctly, as it returns the sublist `[1]` which is the sublist with the minimum length. 

Note that this function will return the first sublist with the minimum length if there are multiple sublists with the same minimum length. If you want to return all sublists with the minimum length, you would need a slightly different function. 

For example, you could use a list comprehension to create a list of all sublists with the minimum length:

```Python
def Find_Min(lst):
    min_len = min(len(x) for x in lst)
    return [x for x in lst if len(x) == min_len]
```  This function will return a list of all sublists with the minimum length. 

You could also use a lambda function to define a custom sorting key and then use the built-in sorted() function to sort the list of sublists by length:

```Python
def Find_Min(lst):
    return sorted(lst, key=len)[0]
```  This function will also return the first sublist with the minimum length. 

Remember that these functions will return the first sublist with the minimum length if there are multiple sublists with the same minimum length. If you want to return all sublists with the minimum length, you would need a different approach. 

Also note that these functions do not handle the case where the input list is empty. You may want to add error handling to handle this case, depending on your specific requirements. 
```
def check_element(lst, element):
    return all(item == element for item in lst)
```


The function `check_element` takes two parameters, `lst` and `element`. It uses the built-in `all` function to check if all items in the list `lst` are equal to the `element`. The `all` function returns `True` if all elements of the iterable (in this case, a generator expression) are true. If at least one element is false, it returns `False`. The generator expression `(item == element for item in lst)` iterates over each item in the list and checks if it is equal to the `element`. If all items are equal, the function returns `True`; otherwise, it returns `False`.  The unit test `assert check_element(["green", "orange", "black", "white"],'blue')==False` confirms that the function works correctly, as it checks if all items in the list are equal to `'blue'`, which is not the case, and returns `False`.  



This function will return `True` if all items in the list are equal to the given element, and `False` otherwise. It can be used to check if a list contains only one type of element. For example, `check_element([1, 1, 1, 1], 1)` will return `True`, while `check_element([1, 2, 3, 4], 1)` will return `False`.  



The time complexity of this function is O(n), where n is the length of the list, because it needs to iterate over each item in the list once. The space complexity is O(1), because it only uses a constant amount of space to store the function's variables.  



This function can be used in a variety of situations where you need to check if a list contains only one type of element. For example, you could use it to validate input data or to check if a list of items meets certain criteria.  



Here is the function again:
```
def check_element(lst, element):
    return all(item == element for item in lst)
```  



And here is an example of how you could use it:
```
my_list = [1, 1, 1, 1]
if check_element(my_list, 1):
    print("The list contains only ones.")
else:
    print("The list contains more than one type of element.")
```  
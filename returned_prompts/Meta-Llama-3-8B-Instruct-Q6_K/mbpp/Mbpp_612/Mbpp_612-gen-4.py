```
def merge(lists):
    return [list(map(lambda x: x[0], lists)), list(map(lambda x: x[1], lists))]
```


This function uses list comprehension and map function to extract the first and second elements from each sublist and return them in two separate lists. The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` ensures that the function works as expected. 

Note: The map function applies a function (in this case a lambda function) to each item in the list and returns a list of the results. The lambda function takes an item from the list and returns the first or second element of the item. The list comprehension then collects these results into two separate lists. 

The time complexity of this function is O(n), where n is the number of sublists in the input list. This is because the function iterates over the input list once. The space complexity is also O(n), because the function returns two lists that can have up to n elements. 
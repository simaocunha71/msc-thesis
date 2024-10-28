```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```



The provided unit test `assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` suggests that the function should sort each sublist in the given list of lists. The function `sort_sublists` achieves this by using a list comprehension to iterate over each sublist, sort it using the built-in `sorted` function, and return a new list with the sorted sublists. 

This solution assumes that the original order of the sublists in the list of lists should be preserved, which is consistent with the provided unit test. If the order of the sublists does not matter, a simpler solution could be used, such as `sorted(list_of_lists)`. However, the provided unit test implies that the order of the sublists should be preserved. 

The time complexity of this solution is O(n*m*log(m)), where n is the number of sublists and m is the maximum length of a sublist. This is because the `sorted` function has a time complexity of O(m*log(m)) and it is called for each sublist. The space complexity is O(n*m), as we need to store the sorted sublists. 
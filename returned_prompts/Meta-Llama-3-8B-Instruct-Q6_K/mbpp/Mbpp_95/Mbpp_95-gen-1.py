You can solve this problem with the following function:

```python
def Find_Min_Length(list_of_lists):
    return min(len(lst) for lst in list_of_lists)
``` 

This function works by using a generator expression inside the min function. The generator expression iterates over each list in the list of lists and calculates the length of each list with the len function. The min function then returns the smallest length from these calculations. 

For example, if you call Find_Min_Length([[1],[1,2]]), it will return 1, which is the length of the smallest list in the list of lists. 

The unit test provided, assert Find_Min_Length([[1],[1,2]]) == 1, will pass with this function. 
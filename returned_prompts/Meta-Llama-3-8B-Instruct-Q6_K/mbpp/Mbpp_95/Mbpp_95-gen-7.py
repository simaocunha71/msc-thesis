```
def Find_Min_Length(list_of_lists):
    return min(len(sublist) for sublist in list_of_lists)
```



Explanation:
This function takes a list of lists as an input. It uses a generator expression to iterate over each sublist in the list of lists, calculates the length of each sublist using the len() function, and then finds the minimum length using the min() function. The result is the length of the smallest sublist in the list of lists. The unit test `assert Find_Min_Length([[1],[1,2]]) == 1` ensures that the function works correctly.
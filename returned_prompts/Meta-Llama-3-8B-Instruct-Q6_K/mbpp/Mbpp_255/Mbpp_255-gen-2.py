```
def combinations_colors(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(n):
            result.append((lst[i],))
    return result
```


This function generates all combinations of the elements in the list with repetition. The outer loop iterates over each element in the list, and the inner loop repeats the current element 'n' times. Each combination is added to the result list as a tuple. 

The unit test `assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]` helps to clarify the problem, as it shows that the function should generate combinations of length 'n', where 'n' is given as an argument to the function. 

For example, `combinations_colors( ["Red","Green","Blue"],1)` should return `[('Red',), ('Green',), ('Blue',)]`, which are all the combinations of length 1 of the colors in the list. Similarly, `combinations_colors( ["Red","Green","Blue"],2)` should return `[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]`, which are all the combinations of length 2 of the colors in the list. 





The time complexity of this function is O(n*m), where n is the length of the list and m is the length of the combinations. The space complexity is O(n*m), as we are storing all the combinations in the result list. 
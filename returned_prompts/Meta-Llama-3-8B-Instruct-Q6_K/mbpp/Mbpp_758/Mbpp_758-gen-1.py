```
def unique_sublists(lst):
    seen = set()
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in seen:
            count_dict[tuple_sublist] += 1
        else:
            seen.add(tuple_sublist)
            count_dict[tuple_sublist] = 1
    return count_dict
```  

This function works by iterating over each sublist in the input list, converting it to a tuple, and then checking if that tuple has been seen before. If it has, the function increments the count for that tuple in the count_dict dictionary. If it hasn't, the function adds it to the seen set and initializes its count in the count_dict dictionary. The function returns the count_dict dictionary at the end.  

The unit test `assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}` ensures that the function works correctly by checking that the function returns the expected dictionary for a given input list.  

The time complexity of this function is O(n), where n is the total number of elements in the input list, because the function iterates over each element in the list once. The space complexity is also O(n), because in the worst case (when all elements are unique), the function stores each element in the seen set and count_dict dictionary.  
```python
def unique_sublists(lst):
    seen = set()
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in seen:
            count_dict[tuple_sublist] += 1
        else:
            seen.add(tuple_sublist)
            count_dict[tuple_sublist] = 1
    return count_dict
```  

This function works by iterating over each sublist in the input list, converting it to a tuple, and then checking if that tuple has been seen before. If it has, the function increments the count for that tuple in the count_dict dictionary. If it hasn't, the function adds it to the seen set and initializes its count in the count_dict dictionary. The function returns the count_dict dictionary at the end.  


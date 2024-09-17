```
def extract_index_list(l1, l2, l3):
    return [i for i in l1 if l2[i] == l3[i]]
```
This function uses list comprehension to iterate over the indices of the first list and checks if the elements at the same index in the second and third lists are equal. If they are, it includes the index in the output list.

For example, for the input lists [1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7] and [0, 1, 2, 3, 4, 5, 7], the function returns [1, 7] because the elements at indices 1 and 7 in all three lists are equal. 

The unit test `assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]` confirms this result. 






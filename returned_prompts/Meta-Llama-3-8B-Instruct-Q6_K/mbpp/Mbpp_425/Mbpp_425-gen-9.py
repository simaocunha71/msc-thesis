```
def count_element_in_list(list_of_lists, element):
    return sum(1 for sublist in list_of_lists if element in sublist)
```


This function iterates over each sublist in the list of lists. For each sublist, it checks if the element is present. If the element is present, it counts it. The sum of these counts is the total number of sublists containing the element. 

The unit test `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` confirms that this function is working correctly. It checks if the function returns 3 when the input is a list of lists and the element is 1, which is the expected output. 






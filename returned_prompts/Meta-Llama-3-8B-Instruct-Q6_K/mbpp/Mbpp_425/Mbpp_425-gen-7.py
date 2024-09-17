```
def count_element_in_list(list_of_lists, target_element):
    count = 0
    for sublist in list_of_lists:
        if target_element in sublist:
            count += 1
    return count
``` 

The function count_element_in_list takes two parameters: a list of lists and a target element. It iterates over each sublist in the list of lists. For each sublist, it checks if the target element is present. If the target element is present, it increments the count. Finally, it returns the count. 

For example, if we call count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1), it will return 3 because the target element 1 is present in three sublists. 

The unit test `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` ensures that the function is working correctly. 
```python
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
``` 
This test checks if the function returns 3 when the target element is 1 and the list of lists is [[1, 3], [5, 7], [1, 11], [1, 15, 7]]. 
```python
``` 
The function is case-sensitive and will not count elements that are not exact matches. For example, if the target element is '1' and one of the sublists contains the string 'one', the function will not count it. 
```python
``` 
If you want a case-insensitive search, you can convert the target element and the elements in the sublists to the same case (either lower or upper) before comparing them. 
```python
``` 
Here is an example of how you can modify the function to make it case-insensitive:
```python
def count_element_in_list(list_of_lists, target_element):
    target_element = target_element.lower()
    count = 0
    for sublist in list_of_lists:
        for element in sublist:
            if element.lower() == target_element:
                count += 1
                break
    return count
``` 
This modified function converts the target element and the elements in the sublists to lower case before
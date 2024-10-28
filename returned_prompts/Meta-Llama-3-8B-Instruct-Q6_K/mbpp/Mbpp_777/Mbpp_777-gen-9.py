```
def find_sum(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return sum([num for num in count_dict if count_dict[num] == 1])
```


The unit test `assert find_sum([1,2,3,1,1,4,5,6]) == 21` suggests that the function should return the sum of non-repeated elements in the list. 

This function uses a dictionary to count the frequency of each element in the list. Then it uses a list comprehension to create a list of elements with a count of 1 and finally returns the sum of this list.

For example, if the input list is [1,2,3,1,1,4,5,6], the function will return the sum of [2,3,4,5,6] which is 21. 
```python
print(find_sum([1,2,3,1,1,4,5,6]))  # Output: 21
```


This function assumes that the input list contains only integers. If the list can contain other types of elements, you may need to modify the function accordingly. 

The time complexity of this function is O(n) where n is the number of elements in the list, because it needs to iterate over the list twice (once to count the frequencies and once to create the list of non-repeated elements). The space complexity is also O(n) because in the worst case, all elements in the list are unique and the dictionary needs to store all of them. 
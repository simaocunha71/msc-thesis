```
def freq_count(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
```


This function iterates over each item in the input list. If the item is already in the frequency dictionary, it increments the count by 1. If the item is not in the dictionary, it adds it with a count of 1. The function then returns the frequency dictionary. The unit test provided ensures that the function works correctly for the given input. 

For example, if the input is [10,10,10,10,20,20,20,20,40,40,50,50,30], the function will return {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}, which is the correct frequency count for each item in the list. 

The time complexity of this function is O(n), where n is the number of elements in the input list, because it iterates over the list once. The space complexity is also O(n), because in the worst case, every element in the list is unique, so the frequency dictionary will have n elements. 

This function is efficient and easy to understand, making it a good solution for this problem. 
```python
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == ({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
``` 
This unit test ensures that the function works correctly for the given input. 
```python
print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
``` 
This will print the frequency count for the given input, which is {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}. 
```python
print(freq_count([1,2,3,4,5,6,7,8,9,10]))
``` 
This will print the frequency count for the given input, which is {1: 1, 2: 1, 3: 1, 4: 1, 
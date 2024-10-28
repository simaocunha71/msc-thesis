```
def freq_count(lst):
    freq = {}
    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq
```


The provided unit test suggests that the function should return a dictionary with the frequency of each element in the list. The function can be implemented using a dictionary to store the frequency of each element. It iterates over the list, and for each element, it checks if the element is already in the dictionary. If it is, it increments the frequency by 1. If not, it adds the element to the dictionary with a frequency of 1. The function then returns the dictionary.

Here is the implementation:
```
def freq_count(lst):
    freq = {}
    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq
```
This function will pass the provided unit test:
```
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == ({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
```


The time complexity of this function is O(n), where n is the number of elements in the list, because it iterates over the list once. The space complexity is also O(n), because in the worst case, the dictionary will contain n elements. 
```
def max_occurrences(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return max(frequency, key=frequency.get)
```



The function `max_occurrences` takes a list as input and returns the item with the maximum frequency in the list. It does this by creating a dictionary `frequency` where the keys are the items in the list and the values are their frequencies. It then returns the key with the maximum value in the dictionary.

For example, if the input list is `[2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]`, the function will return `2` because `2` has the maximum frequency in the list.

The unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` ensures that the function is working correctly. It checks that the function returns `2` when given the list `[2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]`. If the function is working correctly, this test will pass. If the function is not working correctly, this test will fail, indicating that there is an error in the function.
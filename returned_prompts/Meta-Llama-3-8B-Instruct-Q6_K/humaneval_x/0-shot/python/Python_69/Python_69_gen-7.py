```
def search(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    for num in sorted(frequency_dict.keys(), reverse=True):
        if frequency_dict[num] >= num:
            return num

    return -1
```


The function `search(lst)` takes a list of positive integers as an argument. It first creates a dictionary `frequency_dict` where the keys are the numbers in the list and the values are their frequencies. Then, it iterates over the sorted keys in the dictionary in descending order. If it finds a number whose frequency is greater than or equal to the number itself, it returns that number. If no such number is found, it returns -1. 

For example, for the list `[4, 1, 2, 2, 3, 1]`, the function creates a dictionary `{4: 1, 1: 2, 2: 2, 3: 2}`. Then, it iterates over the sorted keys in descending order, which are `[4, 3, 2, 1]`. It finds that the frequency of `2` is `2`, which is greater than or equal to `2`, so it returns `2`. 

For the list `[5, 5, 4, 4, 4]`, the function creates a dictionary `{5: 2, 4: 3}`. Then, it iterates over the sorted keys in descending order, which are `[5, 4]`. It finds that neither `5` nor `4` has a frequency greater than or equal to the number itself, so it returns `-1`. 





The time complexity of the function is O(n log n) due to the sorting operation, where n is the number of unique elements in the list. The space complexity is O(n) for the dictionary. The function returns the correct result for the given examples.
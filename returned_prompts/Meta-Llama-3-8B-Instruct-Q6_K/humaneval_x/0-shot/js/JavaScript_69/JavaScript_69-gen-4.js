Here is a Python solution:

```python
def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(lst)
    for num in freq:
        if num > 0 and freq[num] >= num:
            return num
    return -1
```

In this solution, we first create a frequency dictionary where the keys are the numbers from the list and the values are their frequencies. Then, we iterate over the dictionary to find the maximum frequency that is greater than or equal to the value of the integer itself. If such a value is found, we return it. If not, we return -1. This solution has a time complexity of O(n), where n is the length of the input list.
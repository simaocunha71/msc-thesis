```
def add_elements(arr, k):
    return sum([i for i in arr[:k] if len(str(i)) <= 2])
```


Explanation:
We use a list comprehension to iterate over the first k elements of the array. For each element, we convert it to a string using `str(i)` and check its length. If the length is less than or equal to 2, we include it in the sum. The `sum` function then adds up all these elements. The result is the sum of the elements with at most two digits from the first k elements of the array.
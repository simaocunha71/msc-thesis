```
def add_elements(arr, k):
    return sum(x for x in arr[:k] if len(str(x)) <= 2)
```



This function uses a generator expression to iterate over the first k elements of the array, and then uses the built-in sum function to add up the elements that have at most two digits. The condition `len(str(x)) <= 2` checks whether the number x has at most two digits. The result is the sum of these elements. For example, if `arr = [111,21,3,4000,5,6,7,8,9]` and `k = 4`, the function will return `24`, which is the sum of `21` and `3`.
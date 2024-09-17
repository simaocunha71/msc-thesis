The problem asks you to find the maximum product of a subsequence in an array where the subsequence is increasing. 

The unit test `assert max_product([3, 100, 4, 5, 150, 6]) == 3000` suggests that the product is calculated by multiplying all numbers in the subsequence, not considering the order of the numbers. 

Here is a Python solution for this problem:

```
def max_product(arr):
    if not arr:
        return 0

    max_product = min_product = result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            max_product, min_product, result = min_product, max_product, max(min_product, result)
        max_product *= arr[i]
        min_product = min(min_product, arr[i])

    return result
```

In this solution, we initialize three variables `max_product`, `min_product`, and `result` with the first element of the array. Then we iterate over the array. If the current element is smaller than the previous one, we update `max_product` and `min_product` with the current `min_product` and `max_product` respectively, and update `result` with the maximum of `min_product` and `result`. In each iteration, we update `max_product` by multiplying it with the current element, and update `min_product` with the minimum of the current element and `min_product`. Finally, we return `result` which is the maximum product of the increasing subsequence. 
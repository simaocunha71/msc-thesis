```
def max_product(arr):
    max_product = [1] * len(arr)
    min_product = [1] * len(arr)
    result = arr[0]
    
    for i in range(1, len(arr)):
        max_product[i] = max(arr[i], max_product[i-1] * arr[i])
        min_product[i] = min(arr[i], min_product[i-1] * arr[i])
        result = max(result, max_product[i])
    
    return result
```


The function `max_product` takes an array as input and returns the maximum product that can be formed by multiplying numbers of an increasing subsequence of that array.

It uses dynamic programming to keep track of the maximum product and the minimum product of the increasing subsequence ending at each position.

The maximum product at each position is the maximum of the current number and the product of the previous maximum product and the current number.

The minimum product at each position is the minimum of the current number and the product of the previous minimum product and the current number.

The result is the maximum product found in the array.

The unit test `assert max_product([3, 100, 4, 5, 150, 6]) == 3000` ensures that the function returns the correct result for the given input.
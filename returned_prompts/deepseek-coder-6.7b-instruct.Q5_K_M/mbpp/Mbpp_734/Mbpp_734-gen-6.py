```python
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sum_prod = 0
    for i in range(n):
        if i == 0:
            prod[i] = arr[i]
        else:
            prod[i] = prod[i-1]*arr[i]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l
            if l == 1:
                sum_prod += arr[i]
            else:
                if i == 0:
                    sum_prod += prod[j-1]
                else:
                    sum_prod += prod[j-1]//prod[i-1]
    return sum_prod

print(sum_Of_Subarray_Prod([1,2,3]))
```

The function `sum_Of_Subarray_Prod` takes a list `arr` as input and returns the sum of products of all possible sublists of this list. We first calculate the product of all elements in `arr` till index `i` and store the results in `prod`. Then for every possible sublist (of length 1 to `n`), we calculate the product of its elements and add it to `sum_prod`. 

Finally, we return `sum_prod` which is the sum of products of all possible sublists. 

The function returns 20 for input [1,2,3] as expected.

Please note that the function uses integer division (//) to calculate the product of sublists. This is because the product of sublists might exceed the limit of an integer. The product is calculated by taking the product of elements from index `i` to `j-1` in `prod`.

Also, the function assumes that the list `arr` contains positive integers. If the list contains zero, the function will return zero as there are no sublists of length greater than 1 that contain zero.

This solution has a time complexity of O(n^2) as there are two nested loops. The space complexity is O(n) as we store the product of all elements in `arr` till index `i` in `prod
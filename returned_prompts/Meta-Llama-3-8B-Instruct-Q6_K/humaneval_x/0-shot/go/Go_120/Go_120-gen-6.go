You can solve this problem by using a combination of the `sort` package and a slice to store the maximum k numbers. Here's the implementation:

```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    // Create a slice to store the maximum k numbers
    maxK := make([]int, k)
    
    // Copy the first k elements from arr to maxK
    copy(maxK, arr[:k])
    
    // Sort the maxK slice in descending order
    sort.Slice(maxK, func(i, j int) bool {
        return maxK[i] > maxK[j]
    })
    
    // Create a slice to store the result
    result := make([]int, k)
    
    // Copy the first k elements from maxK to result
    copy(result, maxK)
    
    return result
}
```

This function first creates a slice `maxK` to store the maximum k numbers, then copies the first k elements from `arr` to `maxK`. It then sorts `maxK` in descending order using the `sort.Slice` function. Finally, it creates a new slice `result` to store the result and copies the first k elements from `maxK` to `result`.

For example, if `arr = [-3, -4, 5]` and `k = 3`, the function will return `[-4, -3, 5]`, which are the maximum k numbers in `arr`.

Note that this function assumes that `k` is less than or equal to the length of `arr`. If `k` is greater than the length of `arr`, the function will return the entire `arr` sorted in descending order. If you want to handle this case differently, you can add additional logic to the function.
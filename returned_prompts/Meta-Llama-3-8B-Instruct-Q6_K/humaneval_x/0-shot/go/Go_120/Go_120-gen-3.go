Here is the solution in Go:
```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    // Sort the array in descending order
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    
    // Return the first k elements of the sorted array
    return arr[:k]
}
```
Explanation:

1. We use the `sort.Slice` function to sort the array in descending order. This is done by providing a custom comparison function that returns `true` if the element at index `i` is greater than the element at index `j`.
2. After sorting the array, we return the first `k` elements of the sorted array using slicing (`arr[:k]`).

This solution has a time complexity of O(n log n) due to the sorting step, where `n` is the length of the input array. The space complexity is O(1) since we only use a small amount of extra memory to store the sorted array.
Here is a solution in Go:

```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    // Sort the array
    sort.Ints(arr)
    
    // Return the first k elements
    return arr[:k]
}
```
This solution works by first sorting the input array in ascending order using the `sort.Ints()` function. Then it returns the first `k` elements of the sorted array. This solution assumes that the input array is not `nil` and `k` is within the bounds of the array length.

This solution is simple and efficient, as the sorting operation has a time complexity of O(n log n) and the slicing operation has a time complexity of O(k).
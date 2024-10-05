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
This solution uses the `sort.Slice` function to sort the array in descending order, and then returns the first `k` elements of the sorted array using slicing.

Here's an explanation of the code:

1. `sort.Slice(arr, func(i, j int) bool { return arr[i] > arr[j] })`: This line sorts the array in descending order. The `sort.Slice` function takes two arguments: the first is the array to be sorted, and the second is a function that compares two elements of the array. In this case, the comparison function returns `true` if the first element is greater than the second element, and `false` otherwise. This means that the array will be sorted in descending order.
2. `return arr[:k]`: This line returns the first `k` elements of the sorted array. The `[:k]` syntax is used to slice the array, which returns a new slice that contains the first `k` elements of the original array.

This solution has a time complexity of O(n log n), where `n` is the length of the input array, because it uses the `sort.Slice` function to sort the array. The space complexity is O(1), because it only uses a small amount of extra memory to store the sorted array.
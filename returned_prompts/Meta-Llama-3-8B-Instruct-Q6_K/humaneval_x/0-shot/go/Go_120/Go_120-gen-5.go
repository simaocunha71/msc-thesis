Here is the solution in Golang:
```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    // Create a slice of integers with their indices
    indices := make([]struct{val, idx int}, len(arr))
    for i, val := range arr {
        indices[i].val = val
        indices[i].idx = i
    }
    
    // Sort the slice based on the values in descending order
    sort.Slice(indices, func(i, j int) bool {
        return indices[i].val > indices[j].val
    })
    
    // Return the top k values
    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = indices[i].val
    }
    return result
}
```
Explanation:

1. We create a slice of structs, where each struct contains the value and index of each element in the original array.
2. We sort the slice based on the values in descending order using the `sort.Slice` function.
3. We create a new slice to store the top k values and iterate through the sorted slice, adding each value to the result slice until we reach the desired length k.
4. We return the result slice, which contains the maximum k numbers in the original array.

Note: This solution has a time complexity of O(n log n) due to the sorting, where n is the length of the input array. The space complexity is O(n) for the additional slice created to store the indices.
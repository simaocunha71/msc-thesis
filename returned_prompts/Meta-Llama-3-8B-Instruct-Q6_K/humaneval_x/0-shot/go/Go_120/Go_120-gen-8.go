Here is a Go solution for the problem:

```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    // Create a slice of pairs, where each pair contains the value from the input array and its index
    pairs := make([](int, 2), len(arr))
    for i, x := range arr {
        pairs[i] = (x, i)
    }
    
    // Sort the pairs in descending order based on the value
    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i][0] > pairs[j][0]
    })
    
    // Create a new slice and copy the k largest values from the sorted pairs
    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = pairs[i][0]
    }
    
    // Sort the result slice in ascending order
    sort.Ints(result)
    
    return result
}
```

This solution works by first creating a slice of pairs, where each pair contains a value from the input array and its index. Then, it sorts the pairs in descending order based on the value. After that, it creates a new slice and copies the k largest values from the sorted pairs. Finally, it sorts the result slice in ascending order and returns it.

The time complexity of this solution is O(n log n) due to the sorting operations, where n is the length of the input array. The space complexity is O(n) for storing the pairs and the result slice.
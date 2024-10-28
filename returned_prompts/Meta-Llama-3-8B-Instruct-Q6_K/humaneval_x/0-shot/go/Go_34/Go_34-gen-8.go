Here is the solution using Go's built-in sort package:

```go
import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    // Create a set to keep track of unique elements
    unique := make(map[int]bool)
    for _, v := range l {
        unique[v] = true
    }
    // Convert the map to a slice
    var result []int
    for k := range unique {
        result = append(result, k)
    }
    // Sort the result
    sort.Ints(result)
    return result
}
```

In this solution, we first create a set using a map to keep track of unique elements. Then, we convert the map to a slice and sort it. This ensures that the output is a sorted list of unique elements. Note that the order of elements in the original list is not preserved in the output. If you need to preserve the order, you can use a different approach.
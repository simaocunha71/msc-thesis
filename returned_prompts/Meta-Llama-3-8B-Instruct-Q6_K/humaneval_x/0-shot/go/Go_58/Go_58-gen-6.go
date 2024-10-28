You can solve this problem by using Go programming language. Here is a sample solution:

```go
import (
    "sort"
)

// Return sorted unique Common elements for two lists.
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int, l2 []int) []int {
    // Convert lists to sets for efficient lookup
    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    for _, v := range l1 {
        set1[v] = true
    }
    for _, v := range l2 {
        set2[v] = true
    }
    // Find common elements
    common := make([]int, 0)
    for k := range set1 {
        if set2[k] {
            common = append(common, k)
        }
    }
    // Sort the common elements
    sort.Ints(common)
    return common
}
```

This function first converts the input lists into sets, which allows it to efficiently look up elements. It then iterates over the elements in the first set, and adds any elements that are also in the second set to the result. Finally, it sorts the result and returns it. The time complexity of this function is O(n), where n is the sum of the lengths of the input lists. The space complexity is also O(n), because in the worst case the function needs to store all elements from both lists.
Here is a simple solution using a set and a slice:

```go
import (
    "sort"
)

func Common(l1 []int, l2 []int) []int {
    set := make(map[int]bool)
    for _, v := range l1 {
        set[v] = true
    }
    common := make([]int, 0)
    for _, v := range l2 {
        if set[v] {
            common = append(common, v)
            delete(set, v)
        }
    }
    sort.Ints(common)
    return common
}
```

This function first creates a set from the elements of `l1`. Then it iterates over the elements of `l2`, and if an element is found in the set, it is added to the `common` slice and removed from the set. Finally, the `common` slice is sorted and returned. The time complexity of this function is O(n), where n is the sum of the lengths of `l1` and `l2`. The space complexity is O(n), where n is the length of `l1`.
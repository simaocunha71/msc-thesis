Here is a simple Go function that returns a sorted, unique list of integers. This function uses the `sort` package to sort the list, and a `map` to keep track of unique elements. The `map` is used as a set, where each key is a unique element and its value is ignored.

```go
import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    m := make(map[int]bool)
    var result []int
    for _, val := range l {
        if _, value := m[val]; !value {
            m[val] = true
            result = append(result, val)
        }
    }
    sort.Ints(result)
    return result
}
```

This function iterates over the input list once, creating a map of unique elements. It then iterates over the map to create a new list of unique elements, which it sorts using the `sort.Ints` function. The resulting list is returned.

This function has a time complexity of O(n log n), where n is the length of the input list, due to the sorting step. The space complexity is O(n), as we need to store the unique elements in a list.
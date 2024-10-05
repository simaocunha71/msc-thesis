Here is a Go solution using a slice and the `sort` package to remove duplicates and sort the elements:

```go
import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    // Create a map to store unique elements
    m := make(map[int]bool)
    keys := []int{}
    for _, v := range l {
        if _, value := m[v]; !value {
            m[v] = true
            keys = append(keys, v)
        }
    }
    // Sort the unique elements
    sort.Ints(keys)
    return keys
}
```
This solution works by first creating a map to store unique elements. It then iterates over the input slice and checks if each element is already present in the map. If not, it adds the element to the map and the slice of unique elements. Finally, it sorts the slice of unique elements using the `sort.Ints` function. The resulting slice is then returned. 

Note that the order of elements in the output slice may not be the same as the order in the input slice, since the `sort.Ints` function sorts the slice in ascending order. If you need to preserve the order of elements, you can sort the slice first and then remove duplicates. However, this approach would have a time complexity of O(n log n) due to the sorting. 

The time complexity of this solution is O(n), where n is the length of the input slice. This is because we are iterating over the input slice twice: once to remove duplicates and once to sort the unique elements. The space complexity is also O(n), since we are storing all unique elements in the slice. 
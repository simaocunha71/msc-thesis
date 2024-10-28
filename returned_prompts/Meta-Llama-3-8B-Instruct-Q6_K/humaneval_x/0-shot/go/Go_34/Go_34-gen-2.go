Here is the solution:
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

    // Convert the set to a slice and sort it
    var result []int
    for k := range unique {
        result = append(result, k)
    }
    sort.Ints(result)

    return result
}
```
Explanation:

1. We create a map `unique` to keep track of unique elements from the input list `l`.
2. We iterate over the input list and add each element to the map as a key. If the element is already present in the map, it will not be added again, effectively removing duplicates.
3. We convert the map to a slice `result` and sort it using the `sort.Ints` function.
4. Finally, we return the sorted and unique slice.

Note that this solution assumes that the input list contains only integers. If the input list can contain other types of values, you may need to modify the solution accordingly.
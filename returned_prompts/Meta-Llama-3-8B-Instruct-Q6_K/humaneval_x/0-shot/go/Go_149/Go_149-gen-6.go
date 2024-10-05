Here is a solution using the sort package in Go:

```go
import (
    "sort"
)

func SortedListSum(lst []string) []string {
    // Filter out the strings with odd lengths
    filtered := make([]string, 0)
    for _, s := range lst {
        if len(s)%2 == 0 {
            filtered = append(filtered, s)
        }
    }

    // Sort the filtered list by length and then alphabetically
    sort.SliceStable(filtered, func(i, j int) bool {
        if len(filtered[i]) == len(filtered[j]) {
            return filtered[i] < filtered[j]
        }
        return len(filtered[i]) < len(filtered[j])
    })

    return filtered
}
```

This function first filters out the strings with odd lengths from the input list, then sorts the filtered list by length and then alphabetically. The `sort.SliceStable` function is used to sort the list, and the comparison function ensures that strings with the same length are sorted alphabetically. The resulting list is then returned.
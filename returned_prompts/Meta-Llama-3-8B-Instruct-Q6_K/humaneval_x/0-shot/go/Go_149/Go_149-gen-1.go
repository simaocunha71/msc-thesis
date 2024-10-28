Here is a Go function that implements the described behavior:

```go
func SortedListSum(lst []string) []string {
    // Filter out strings with odd length
    filtered := make([]string, 0)
    for _, str := range lst {
        if len(str)%2 == 0 {
            filtered = append(filtered, str)
        }
    }

    // Sort the list by length and then alphabetically
    sort.Slice(filtered, func(i, j int) bool {
        if len(filtered[i]) < len(filtered[j]) {
            return true
        } else if len(filtered[i]) == len(filtered[j]) {
            return filtered[i] < filtered[j]
        }
        return false
    })

    return filtered
}
```

This function first creates a new slice `filtered` and appends only the strings with even lengths from the input slice `lst`. Then it sorts the `filtered` slice using the `sort.Slice` function, which sorts the slice based on the provided comparison function. The comparison function first compares the lengths of the strings, and if they are equal, it compares them alphabetically. Finally, the function returns the sorted `filtered` slice.
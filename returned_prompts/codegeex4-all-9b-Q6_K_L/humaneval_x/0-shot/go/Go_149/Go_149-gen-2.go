Here is a possible implementation of the function in Go:

```go
func SortedListSum(lst []string) []string {
    // Filter out the strings with odd lengths
    filtered := make([]string, 0)
    for _, str := range lst {
        if len(str)%2 == 0 {
            filtered = append(filtered, str)
        }
    }

    // Sort the filtered list by length and then alphabetically
    sort.Slice(filtered, func(i, j int) bool {
        if len(filtered[i]) == len(filtered[j]) {
            return filtered[i] < filtered[j]
        }
        return len(filtered[i]) < len(filtered[j])
    })

    return filtered
}
```

This implementation first filters out the strings with odd lengths from the input list. Then it sorts the filtered list by length and then alphabetically using the `sort.Slice` function. Finally, it returns the sorted list.
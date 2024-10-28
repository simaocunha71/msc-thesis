```go
func SortedListSum(lst []string) []string {
    // create a new slice to store strings with even lengths
    even := []string{}
    // iterate over the input slice
    for _, v := range lst {
        // if the length of the string is even, add it to the new slice
        if len(v)%2 == 0 {
            even = append(even, v)
        }
    }
    // sort the new slice alphabetically
    sort.Strings(even)
    // sort the new slice by length
    sort.Slice(even, func(i, j int) bool {
        return len(even[i]) < len(even[j])
    })
    // return the sorted slice
    return even
}
```
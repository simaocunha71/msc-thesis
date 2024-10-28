```go
func SortedListSum(lst []string) []string {
    // Filter the strings with odd lengths
    filteredList := make([]string, 0)
    for _, s := range lst {
        if len(s)%2 == 0 {
            filteredList = append(filteredList, s)
        }
    }

    // Sort the filtered list by length and then alphabetically
    sort.Slice(filteredList, func(i, j int) bool {
        if len(filteredList[i]) == len(filteredList[j]) {
            return filteredList[i] < filteredList[j]
        }
        return len(filteredList[i]) < len(filteredList[j])
    })

    return filteredList
}
```

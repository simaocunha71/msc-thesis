```go
func SortedListSum(lst []string) []string {
    // Step 1: Delete strings with odd lengths
    var res []string
    for _, s := range lst {
        if len(s)%2 == 0 {
            res = append(res, s)
        }
    }
    
    // Step 2: Sort the list by length and then alphabetically
    sort.Slice(res, func(i, j int) bool {
        if len(res[i]) == len(res[j]) {
            return res[i] < res[j]
        }
        return len(res[i]) < len(res[j])
    })
    
    return res
}
```

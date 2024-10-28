```go
func SortedListSum(lst []string) []string {
    // filter out strings with odd lengths
    filtered := make([]string, 0)
    for _, str := range lst {
        if len(str)%2 == 0 {
            filtered = append(filtered, str)
        }
    }
    
    // sort the filtered list by length and then alphabetically
    sort.SliceStable(filtered, func(i, j int) bool {
        if len(filtered[i]) != len(filtered[j]) {
            return len(filtered[i]) < len(filtered[j])
        }
        return filtered[i] < filtered[j]
    })
    
    return filtered
}
``` 
This function first filters out the strings with odd lengths by iterating through the input list and adding strings with even lengths to a new slice. Then it sorts the filtered list using the `sort.SliceStable` function, which preserves the original order of equal elements. The sorting is done by comparing the lengths of the strings first, and if the lengths are equal, it sorts alphabetically. The function finally returns the sorted list. 
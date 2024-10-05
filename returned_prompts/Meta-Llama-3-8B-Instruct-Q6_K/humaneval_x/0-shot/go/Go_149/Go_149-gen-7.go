```go
func SortedListSum(lst []string) []string {
    sort.SliceStable(lst, func(i, j int) bool {
        if len(lst[i]) != len(lst[j]) {
            return len(lst[i]) < len(lst[j])
        }
        return lst[i] < lst[j]
    })
    return filterOddLength(lst)
}

func filterOddLength(lst []string) []string {
    var result []string
    for _, str := range lst {
        if len(str)%2 == 0 {
            result = append(result, str)
        }
    }
    return result
}
```
This solution uses the `sort.SliceStable` function to sort the list of strings. The comparison function passed to `sort.SliceStable` first compares the lengths of the strings. If the lengths are different, it returns `true` if the first string has a smaller length, and `false` otherwise. If the lengths are the same, it compares the strings lexicographically (i.e., alphabetically).

After sorting the list, the `filterOddLength` function is used to remove the strings with odd lengths. This function iterates over the list, and for each string, it checks if the length is even. If it is, the string is added to the result list.

The `SortedListSum` function returns the result list after filtering and sorting. The `filterOddLength` function is used to filter out the strings with odd lengths, and the `sort.SliceStable` function is used to sort the list based on the length and then alphabetically. The sorted list is then returned.
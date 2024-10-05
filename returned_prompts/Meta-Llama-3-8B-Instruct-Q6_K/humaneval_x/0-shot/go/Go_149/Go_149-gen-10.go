```go
func SortedListSum(lst []string) []string {
    sort.SliceStable(lst, func(i, j int) bool {
        if len(lst[i]) != len(lst[j]) {
            return len(lst[i]) < len(lst[j])
        }
        return lst[i] < lst[j]
    })
    return filterEvenLength(lst)
}

func filterEvenLength(lst []string) []string {
    result := make([]string, 0)
    for _, str := range lst {
        if len(str)%2 == 0 {
            result = append(result, str)
        }
    }
    return result
}
```


This solution first sorts the list of strings based on their lengths and then alphabetically. It uses the `sort.SliceStable` function from the Go standard library, which sorts the list in ascending order based on the given function. The function returns `true` if the first element should come before the second in the sorted order.

The `filterEvenLength` function filters out the strings that have odd lengths from the list. It iterates over the list, checks the length of each string, and if the length is even, it appends the string to the result list.

The `SortedListSum` function first sorts the list and then filters out the strings with odd lengths. It returns the resulted list. The unit tests provided ensure that the function works correctly. For example, the test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` checks that the function correctly filters out the strings with odd lengths and sorts the remaining strings alphabetically.
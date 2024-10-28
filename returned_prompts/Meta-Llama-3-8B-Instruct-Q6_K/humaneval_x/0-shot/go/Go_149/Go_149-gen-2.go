```go
func SortedListSum(lst []string) []string {
    // Filter out strings with odd lengths
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


The provided Go function `SortedListSum` takes a list of strings `lst` as input, filters out the strings with odd lengths, and returns the resulted list sorted by the length of each word in ascending order. If two words have the same length, it sorts the list alphabetically.

The function uses the `sort.Slice` function from the `sort` package to sort the filtered list. The custom comparison function provided to `sort.Slice` checks if the lengths of the two strings are equal. If they are equal, it compares the strings alphabetically using the `<` operator. If the lengths are not equal, it compares the lengths. The function appends the filtered and sorted list to the original list.

The function then returns the filtered and sorted list. The unit tests provided ensure that the function works correctly for the given examples. For instance, the test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` checks that the function returns the list `["aa"]` when given the input `["aa", "a", "aaa"]`. Similarly, the test `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]` checks that the function returns the list `["ab", "cd"]` when given the input `["ab", "a", "aaa", "cd"]`. These tests ensure that the function works correctly for different inputs.
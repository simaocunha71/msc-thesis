```go
func SortedListSum(lst []string) []string {
    sort.SliceStable(lst, func(i, j int) bool {
        if len(lst[i]) != len(lst[j]) {
            return len(lst[i]) < len(lst[j])
        }
        return lst[i] < lst[j]
    })
    result := []string{}
    for _, str := range lst {
        if len(str)%2 == 0 {
            result = append(result, str)
        }
    }
    return result
}
```



Explanation:
The function `SortedListSum` takes a list of strings as input, removes the strings with odd lengths, and returns the resulting list in a sorted order.

The function first sorts the list in a stable manner using the `sort.SliceStable` function. The sorting criteria are as follows:

1. If the lengths of the strings are different, sort by length in ascending order.
2. If the lengths are the same, sort alphabetically.

After sorting the list, the function iterates over the list and appends the strings with even lengths to a new list `result`.

Finally, the function returns the `result` list. The time complexity of this function is O(n log n) due to the sorting, where n is the length of the input list. The space complexity is O(n) for storing the result list.
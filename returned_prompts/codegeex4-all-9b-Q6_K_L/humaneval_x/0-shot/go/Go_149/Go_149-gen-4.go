```go
func SortedListSum(lst []string) []string {
    sortedList := make([]string, 0)
    for _, word := range lst {
        if len(word)%2 == 0 {
            sortedList = append(sortedList, word)
        }
    }
    sort.Slice(sortedList, func(i, j int) bool {
        if len(sortedList[i]) == len(sortedList[j]) {
            return sortedList[i] < sortedList[j]
        }
        return len(sortedList[i]) < len(sortedList[j])
    })
    return sortedList
}
```

This function iterates through the input list, appending only the strings of even length to the sortedList. After that, it sorts the sortedList first by the length of the strings and then alphabetically if the lengths are equal. The sorted and filtered list is then returned.
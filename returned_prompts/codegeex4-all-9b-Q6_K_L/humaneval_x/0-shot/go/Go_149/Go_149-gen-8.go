Here is a Go solution for your problem:

```go
func SortedListSum(lst []string) []string {
    // Filter out strings with odd lengths
    var filteredList []string
    for _, str := range lst {
        if len(str) % 2 == 0 {
            filteredList = append(filteredList, str)
        }
    }
    
    // Sort the list by length and alphabetically
    sort.SliceStable(filteredList, func(i, j int) bool {
        if len(filteredList[i]) == len(filteredList[j]) {
            return filteredList[i] < filteredList[j]
        }
        return len(filteredList[i]) < len(filteredList[j])
    })

    return filteredList
}
```

In this code, we first create a new slice `filteredList` which only contains strings with even lengths. We then sort this slice by length and alphabetically using the `sort.SliceStable` function. This function accepts a slice and a less function as arguments. The less function is a function that takes two indices of the slice and returns a boolean indicating whether the element at the first index should come before the element at the second index in the sorted slice. We define this less function to first compare the lengths of the two strings and then compare the strings alphabetically if the lengths are the same.
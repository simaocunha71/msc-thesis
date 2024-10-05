You can use the `strings.Contains` function to check if a string contains a given substring, and then use the `filter` function to filter out the strings that don't contain the substring:

```go
func FilterBySubstring(stringList []string, substring string) []string {
    var filteredList []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }
    return filteredList
}
```

This function iterates over each string in the input list, and if the string contains the given substring, it adds it to the `filteredList`. Finally, it returns the `filteredList`.
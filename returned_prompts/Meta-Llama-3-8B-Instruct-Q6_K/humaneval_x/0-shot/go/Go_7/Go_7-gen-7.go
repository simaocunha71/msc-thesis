Here is the solution to the problem:

```go
import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
// ['abc', 'bacd', 'array']
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


In this solution, we use the `strings.Contains` function to check if a given string in the input list contains the specified substring. If it does, we add it to the `filteredList`. Finally, we return the `filteredList`. This function iterates over the input list and checks each string, making it efficient for large lists.
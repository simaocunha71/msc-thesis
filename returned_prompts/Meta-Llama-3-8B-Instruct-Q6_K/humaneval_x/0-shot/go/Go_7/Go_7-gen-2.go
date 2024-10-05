Here is the solution in Go:

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
    var result []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}
```



This function iterates over each string in the input list. For each string, it checks if the string contains the given substring using the `strings.Contains` function. If the string contains the substring, it is added to the result list. Finally, the function returns the result list.
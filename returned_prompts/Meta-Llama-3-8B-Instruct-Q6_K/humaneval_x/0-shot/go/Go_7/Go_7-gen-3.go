Here is the solution:

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
    result := make([]string, 0)
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}
```


Explanation:

1. We create an empty slice `result` to store the filtered strings.
2. We iterate over the input slice `stringList` using a range loop.
3. For each string `str` in the list, we check if it contains the given `substring` using the `strings.Contains` function.
4. If the string contains the substring, we append it to the `result` slice.
5. Finally, we return the filtered `result` slice.
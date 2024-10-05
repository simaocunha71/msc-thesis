Here is a simple implementation of the `FilterBySubstring` function in Go:

```go
package main

import (
    "strings"
    "fmt"
)

// Filter an input list of strings only for ones that contain given substring
func FilterBySubstring(stringList []string, substring string) []string {
    var result []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}

func main() {
    fmt.Println(FilterBySubstring([]string{}, 'a')) // []
    fmt.Println(FilterBySubstring([]string{"abc", "bacd", "cde", "array"}, 'a')) // ["abc", "bacd", "array"]
}
```

In this code, we use the `strings.Contains` function to check if a string contains the given substring. If it does, we append it to the result slice. Finally, we return the result slice. The `main` function demonstrates the usage of `FilterBySubstring` with some examples.
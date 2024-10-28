You can use the strings package in Go to achieve this. The ToUpper() and ToLower() functions convert all lowercase and uppercase characters to their opposite. Here's how you could implement FlipCase():

```go
import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
func FlipCase(str string) string {
    return strings.ToTitle(strings.ToLower(str))
}
```

In this function, strings.ToLower(str) converts all uppercase characters in the string to lowercase and strings.ToTitle() converts all lowercase characters to uppercase.
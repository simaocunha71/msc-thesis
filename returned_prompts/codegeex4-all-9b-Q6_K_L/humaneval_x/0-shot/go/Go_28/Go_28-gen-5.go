You can concatenate a slice of strings into a single string using the `strings.Join()` function in Go. Here's a modified version of your `Concatenate` function that uses `strings.Join()`:

```go
package main

import (
    "fmt"
    "strings"
)

func Concatenate(strings []string) string {
    return strings.Join(strings, "")
}

func main() {
    fmt.Println(Concatenate([]string{}))       // Output: ""
    fmt.Println(Concatenate([]string{"a", "b", "c"})) // Output: "abc"
}
```

In this function, `strings.Join(strings, "")` takes a slice of strings and joins them into a single string without any separator.
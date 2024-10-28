You can use a regular expression to match two or more consecutive spaces and replace them with a dash. Then, replace all remaining spaces with underscores. Here's the solution in Go:

```go
package main

import (
    "fmt"
    "regexp"
)

func FixSpaces(text string) string {
    // Replace two or more consecutive spaces with a dash
    text = regexp.MustCompile(`\s{2,}`).ReplaceAllString(text, "-")
    // Replace remaining spaces with underscores
    text = regexp.MustCompile(`\s`).ReplaceAllString(text, "_")
    return text
}

func main() {
    fmt.Println(FixSpaces("Example"))          // Output: "Example"
    fmt.Println(FixSpaces("Example 1"))        // Output: "Example_1"
    fmt.Println(FixSpaces(" Example 2"))       // Output: "_Example_2"
    fmt.Println(FixSpaces(" Example   3"))     // Output: "_Example-3"
}
```

This solution uses the `regexp` package to match patterns in the string. The `ReplaceAllString` function is used to replace all occurrences of the pattern with the specified replacement.
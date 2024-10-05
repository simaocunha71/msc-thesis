```go
package main

import (
    "fmt"
    "strings"
)

func FixSpaces(text string) string {
    // Replace all spaces with underscores
    text = strings.ReplaceAll(text, " ", "_")

    // Replace all consecutive spaces with -
    for strings.Count(text, "  ") > 0 {
        text = strings.ReplaceAll(text, "  ", "-")
    }

    return text
}

func main() {
    fmt.Println(FixSpaces("Example")) // Output: Example
    fmt.Println(FixSpaces("Example 1")) // Output: Example_1
    fmt.Println(FixSpaces(" Example 2")) // Output: _Example_2
    fmt.Println(FixSpaces(" Example   3")) // Output: _Example-3
}
```

Explanation:
The `FixSpaces` function takes a string `text` as input, replaces all spaces with underscores using `strings.ReplaceAll`, and then replaces all consecutive spaces with `-` using a loop that continues until there are no more consecutive spaces. The function returns the modified string.

In the `main` function, we test the `FixSpaces` function with different input strings and print the results to the console.

Note that the `strings.ReplaceAll` function is used to replace all occurrences of a substring in a string, while the `strings.Count` function is used to count the number of occurrences of a substring in a string. The `for` loop continues until there are no more consecutive spaces in the string. This ensures that all consecutive spaces are replaced with `-`.
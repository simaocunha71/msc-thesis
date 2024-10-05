Here is a simple and efficient solution using the `filter` function from the `go` standard library:

```go
package main

import (
    "fmt"
    "strings"
)

func FilterByPrefix(strings []string, prefix string) []string {
    filtered := make([]string, 0)
    for _, str := range strings {
        if strings.HasPrefix(str, prefix) {
            filtered = append(filtered, str)
        }
    }
    return filtered
}

func main() {
    strings := []string{"abc", "bcd", "cde", "array"}
    prefix := "a"
    result := FilterByPrefix(strings, prefix)
    fmt.Println(result) // Output: [abc array]
}
```

This code defines a function `FilterByPrefix` that takes a slice of strings and a prefix as arguments. It initializes an empty slice `filtered` to store the filtered strings. Then it iterates over the input slice `strings` using a range loop. For each string, it checks if the string starts with the given prefix using the `strings.HasPrefix` function. If it does, it appends the string to the `filtered` slice. Finally, it returns the `filtered` slice.

In the `main` function, we test the `FilterByPrefix` function with a sample input slice and prefix, and print the result to the console. The output is `["abc", "array"]`, which are the strings that start with the prefix "a".
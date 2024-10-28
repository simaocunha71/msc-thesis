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
    fmt.Println(Concatenate([]string{})) // prints ''
    fmt.Println(Concatenate([]string{"a", "b", "c"})) // prints 'abc'
}
```

Explanation:
The `Concatenate` function takes a slice of strings as input and returns a single string that is the concatenation of all the strings in the slice. The `strings.Join` function is used to concatenate the strings. The second argument to `strings.Join` is an empty string, which means that the strings in the slice are concatenated without any separator in between.

In the `main` function, we call `Concatenate` with an empty slice of strings and a slice containing the strings "a", "b", and "c". The output of the program is printed to the console. The first call to `Concatenate` returns an empty string, and the second call returns the concatenation of the three strings, which is "abc".
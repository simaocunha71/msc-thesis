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
	fmt.Println(Concatenate([]string{}))  // ''
	fmt.Println(Concatenate([]string{"a", "b", "c"}))  // abc
}
```

Explanation:

The `Concatenate` function takes a slice of strings as input and returns a single string that is the concatenation of all the strings in the slice. The `strings.Join` function is used to concatenate the strings. The first argument to `Join` is the slice of strings to be joined, and the second argument is the separator to use between each string. In this case, we use an empty string (`""`), which means that no separator is used and the strings are joined directly.

In the `main` function, we test the `Concatenate` function with an empty slice and a non-empty slice. The output is as expected: an empty string for an empty slice, and the concatenated string "abc" for a non-empty slice.
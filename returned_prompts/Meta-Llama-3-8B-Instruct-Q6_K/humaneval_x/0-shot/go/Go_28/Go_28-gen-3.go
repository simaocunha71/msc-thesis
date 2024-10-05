```go
package main

import (
	"fmt"
)

func Concatenate(strings []string) string {
	var result string
	for _, s := range strings {
		result += s
	}
	return result
}

func main() {
	fmt.Println(Concatenate([]string{}))  // ''
	fmt.Println(Concatenate([]string{"a", "b", "c"}))  // 'abc'
}
```

The `Concatenate` function takes a slice of strings as input and returns a single string that is the concatenation of all the strings in the input slice.

In the `main` function, we test the `Concatenate` function with an empty slice of strings and a non-empty slice of strings. The output is printed to the console using `fmt.Println`. The output is as expected: an empty string when the input slice is empty, and the concatenation of the strings when the input slice is non-empty.
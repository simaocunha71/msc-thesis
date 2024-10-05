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
	fmt.Println(Concatenate([]string{})) // ''
	fmt.Println(Concatenate([]string{"a", "b", "c"})) // 'abc'
}
```

Explanation:

*   The `Concatenate` function takes a slice of strings as input and returns a single string.
*   The function initializes an empty string `result`.
*   It iterates over the input slice using a `for` loop and appends each string in the slice to `result` using the `+=` operator.
*   Finally, it returns the concatenated string.
*   In the `main` function, we test the `Concatenate` function with an empty slice and a slice containing three strings. The output is as expected: an empty string and the concatenated string 'abc'.
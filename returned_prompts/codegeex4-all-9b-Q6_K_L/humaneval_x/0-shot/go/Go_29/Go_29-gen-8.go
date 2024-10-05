Here is a possible solution in Go:

```go
package main

import (
	"fmt"
	"strings"
)

func FilterByPrefix(strings []string, prefix string) []string {
	var result []string
	for _, s := range strings {
		if strings.HasPrefix(s, prefix) {
			result = append(result, s)
		}
	}
	return result
}

func main() {
	fmt.Println(FilterByPrefix([]string{}, "a"))                      // []
	fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a")) // ["abc", "array"]
}
```

The `strings.HasPrefix` function checks whether a string starts with the given prefix. If it does, the string is appended to the result slice.

I hope this helps! Let me know if you have any further questions.
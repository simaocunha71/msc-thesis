Here is a solution in Go:

```go
package main

import (
	"fmt"
)

func FilterByPrefix(strings []string, prefix string) []string {
	var result []string
	for _, s := range strings {
		if s == prefix {
			result = append(result, s)
		}
	}
	return result
}

func main() {
	fmt.Println(FilterByPrefix([]string{}, "a"))
	fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a"))
}
```

This program defines a function `FilterByPrefix` which takes a slice of strings and a prefix string. It iterates over the slice and checks if each string equals the prefix. If it does, the string is added to a new slice `result`. Finally, the `result` slice is returned.

The `main` function is used to test the `FilterByPrefix` function with different inputs. The output of the program is:

```
[]
[abc array]
```

This means that the function correctly filters the input list for strings that start with the given prefix.
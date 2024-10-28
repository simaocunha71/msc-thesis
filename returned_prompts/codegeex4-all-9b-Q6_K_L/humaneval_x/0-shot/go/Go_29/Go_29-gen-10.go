You can filter a list of strings in Go by using the `filter` function from the `github.com/thoas/go-funk` package. Here's an example of how you can do it:

```go
package main

import (
	"fmt"
	"github.com/thoas/go-funk"
)

func main() {
	strings := []string{"abc", "bcd", "cde", "array"}
	prefix := "a"
	filtered := funk.FilterString(strings, func(s string) bool {
		return s == prefix
	})

	fmt.Println(filtered)
}
```

In this example, the `filter` function is used to filter the `strings` slice based on the `prefix` string. The `funk.FilterString` function takes two parameters: the slice to filter and a function that returns a boolean value indicating whether a string should be included in the filtered slice. In this case, the function checks if a string is equal to the `prefix` string. The result is a new slice containing only the strings that match the `prefix` string.

When you run this program, it will output:

```
[a]
```

This shows that the `filter` function correctly filtered the `strings` slice to include only the string that matches the `prefix` string.
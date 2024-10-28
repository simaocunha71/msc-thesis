You can use the `strings.Join()` function to concatenate a slice of strings into a single string. The `strings.Join()` function takes two arguments: the slice of strings to concatenate and a separator string. If the separator string is empty, the strings will be concatenated without any separator.

Here's an example of how to use `strings.Join()` to concatenate a list of strings:

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
	fmt.Println(Concatenate([]string{"a", "b", "c"})) // Output: abc
}
```

In this example, the `Concatenate()` function takes a slice of strings and uses the `strings.Join()` function to concatenate them without any separator. The resulting string is then returned.
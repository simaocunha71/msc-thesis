You can concatenate a slice of strings into a single string in Go by using the strings.Join() function. Here's how you can implement the Concatenate function:

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
	fmt.Println(Concatenate([]string{}))        // Output: ""
	fmt.Println(Concatenate([]string{"a", "b", "c"})) // Output: "abc"
}
```

In the Concatenate function, we pass the slice of strings and an empty separator ("" in this case) to strings.Join(). The function then concatenates all the strings in the slice into a single string, with no separator between them.

In the main function, we test the Concatenate function with an empty slice and a slice containing the strings "a", "b", and "c". The expected output is printed to the console.
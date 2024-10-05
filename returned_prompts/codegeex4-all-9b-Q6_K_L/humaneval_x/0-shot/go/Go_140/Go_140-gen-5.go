You can solve this by using the strings package in Go. Here is an example of how you can do it:

```go
package main

import (
	"strings"
)

func FixSpaces(text string) string {
	text = strings.Replace(text, " ", "_", -1)
	text = strings.Replace(text, "___", "-", -1)
	return text
}

func main() {
	println(FixSpaces("Example"))       // Output: Example
	println(FixSpaces("Example 1"))     // Output: Example_1
	println(FixSpaces(" Example 2"))    // Output: _Example_2
	println(FixSpaces(" Example   3"))  // Output: _Example-3
}
```

In this example, we first replace all spaces with underscores using `strings.Replace`. Then, we replace all 3 consecutive underscores with a dash using `strings.Replace` again. This ensures that only 3 consecutive spaces are replaced, not more.

You can test this function by running the `main` function.
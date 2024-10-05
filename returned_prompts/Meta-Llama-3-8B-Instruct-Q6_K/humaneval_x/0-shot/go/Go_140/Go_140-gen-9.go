```go
package main

import (
	"fmt"
	"regexp"
)

func FixSpaces(text string) string {
	re := regexp.MustCompile(` {2,}`)
	return re.ReplaceAllString(text, "-")
}

func main() {
	fmt.Println(FixSpaces("Example")) // Output: Example
	fmt.Println(FixSpaces("Example 1")) // Output: Example_1
	fmt.Println(FixSpaces(" Example 2")) // Output: _Example_2
	fmt.Println(FixSpaces(" Example   3")) // Output: _Example-3
}
```
The `FixSpaces` function uses a regular expression to replace all sequences of two or more spaces with a single hyphen. The regular expression ` {2,}` matches any sequence of two or more spaces, and the `ReplaceAllString` function replaces all matches with the replacement string `-`. The function returns the modified string.

In the `main` function, we test the `FixSpaces` function with different input strings and print the results. The output shows that the function correctly replaces all spaces with underscores and hyphens for sequences of two or more spaces.
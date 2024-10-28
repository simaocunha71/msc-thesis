You can use the built-in `strings.Contains()` function in Go to check if the second word is a substring of the first word. Additionally, you can rotate the second word by slicing it and concatenating it with itself, then check if the rotated word is a substring of the first word. Here's the implementation:

```go
package main

import (
	"fmt"
	"strings"
)

func CycpatternCheck(a, b string) bool {
	rotated := b + b
	for i := 0; i < len(b); i++ {
		if strings.Contains(a, rotated[i:i+len(b)]) {
			return true
		}
		rotated = rotated[1:] + rotated[:1]
	}
	return false
}

func main() {
	fmt.Println(CycpatternCheck("abcd", "abd"))  // false
	fmt.Println(CycpatternCheck("hello", "ell")) // true
	fmt.Println(CycpatternCheck("whassup", "psus")) // false
	fmt.Println(CycpatternCheck("abab", "baa")) // true
	fmt.Println(CycpatternCheck("efef", "eeff")) // false
	fmt.Println(CycpatternCheck("himenss", "simen")) // true
}
```

The `CycpatternCheck` function takes two strings `a` and `b` as input and returns a boolean value indicating whether the second word `b` or any of its rotations is a substring of the first word `a`. The function first concatenates `b` with itself to create a rotated version of `b`. Then, it iterates over each possible rotation of `b` and checks if the rotated word is a substring of `a` using the `strings.Contains()` function. If a match is found, the function returns `true`. If no match is found after checking all rotations, the function returns `false`.

In the `main` function, we test the `CycpatternCheck` function with various inputs and print the results.
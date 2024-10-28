You can solve this problem by rotating the second word and checking if it is a substring of the first word. Here is a possible solution in Go:

```go
package main

import (
	"fmt"
	"strings"
)

func CycpatternCheck(a, b string) bool {
	n := len(b)
	for i := 0; i < n; i++ {
		b = b[n-1:] + b[:n-1]
		if strings.Contains(a, b) {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(CycpatternCheck("abcd", "abd")) // false
	fmt.Println(CycpatternCheck("hello", "ell")) // true
	fmt.Println(CycpatternCheck("whassup", "psus")) // false
	fmt.Println(CycpatternCheck("abab", "baa")) // true
	fmt.Println(CycpatternCheck("efef", "eeff")) // false
	fmt.Println(CycpatternCheck("himenss", "simen")) // true
}
```

In this solution, we iterate through all possible rotations of the second word and check if it is a substring of the first word using the `strings.Contains` function. If a rotation is found to be a substring, we return `true`. If no rotation is found to be a substring, we return `false`.
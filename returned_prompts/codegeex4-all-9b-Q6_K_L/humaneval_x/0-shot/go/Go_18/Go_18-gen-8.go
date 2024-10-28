You can use the `strings.Count` function in the standard library to count the number of times a substring appears in a string. The `Count` function takes two arguments: the string to search in and the substring to search for. It returns the number of occurrences of the substring in the string.

Here's an example implementation:

```go
package main

import (
	"fmt"
	"strings"
)

func HowManyTimes(str, substring string) int {
	return strings.Count(str, substring)
}

func main() {
	fmt.Println(HowManyTimes("", "a"))         // 0
	fmt.Println(HowManyTimes("aaa", "a"))      // 3
	fmt.Println(HowManyTimes("aaaa", "aa"))    // 3
	fmt.Println(HowManyTimes("aaaab", "aa"))   // 3
	fmt.Println(HowManyTimes("aaaaaa", "aaa")) // 2
}
```

In this implementation, the `HowManyTimes` function simply calls the `strings.Count` function and returns the result. The `main` function demonstrates how to use the `HowManyTimes` function with different inputs.
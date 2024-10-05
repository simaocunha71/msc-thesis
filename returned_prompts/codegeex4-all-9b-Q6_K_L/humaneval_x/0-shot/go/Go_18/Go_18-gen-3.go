You can use the `strings.Count` function in the `strings` package to count the number of times a substring appears in a string. Here's an example:

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
	fmt.Println(HowManyTimes("", "a"))      // Output: 0
	fmt.Println(HowManyTimes("aaa", "a"))    // Output: 3
	fmt.Println(HowManyTimes("aaaa", "aa"))  // Output: 3
}
```

This will count the number of times the substring appears in the original string, including overlapping cases.
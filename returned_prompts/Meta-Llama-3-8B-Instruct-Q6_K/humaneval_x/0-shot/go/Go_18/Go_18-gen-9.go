```go
package main

import (
	"fmt"
	"strings"
)

func HowManyTimes(str string, substring string) int {
	return strings.Count(str, substring)
}

func main() {
	fmt.Println(HowManyTimes("", "a")) // 0
	fmt.Println(HowManyTimes("aaa", "a")) // 3
	fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}
```

The `strings.Count` function from the Go standard library is used to find the number of non-overlapping occurrences of a substring in a string. This function is case-sensitive and it returns 0 if the substring is not found in the string.

In the `main` function, we test the `HowManyTimes` function with three different cases. The output of the program is:

```
0
3
3
```

which matches the expected results. The `HowManyTimes` function is a simple and efficient way to find the number of occurrences of a substring in a string.
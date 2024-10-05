```go
package main

import (
	"fmt"
)

func HowManyTimes(str string, substring string) int {
	count := 0
	strLen := len(str)
	substrLen := len(substring)
	for i := 0; i <= strLen-substrLen; i++ {
		if str[i:i+substrLen] == substring {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a")) // 0
	fmt.Println(HowManyTimes("aaa", "a")) // 3
	fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}
```

This program defines a function `HowManyTimes` that takes two strings, `str` and `substring`, as input. It returns the number of times `substring` can be found in `str`, counting overlapping cases.

In the `main` function, we test the `HowManyTimes` function with three examples:
- `HowManyTimes("", "a")`: The empty string doesn't contain any occurrences of "a", so the result is 0.
- `HowManyTimes("aaa", "a")`: The string "aaa" contains three occurrences of "a", so the result is 3.
- `HowManyTimes("aaaa", "aa")`: The string "aaaa" contains two occurrences of "aa", so the result is 2.

The `HowManyTimes` function works by iterating over the input string `str` and checking each substring of length `substrLen` (the length of the `substring`) to see if it matches the `substring`. If a match is found, the count is incremented. This process is repeated until the end of the input string is reached. The final count is returned as the result.
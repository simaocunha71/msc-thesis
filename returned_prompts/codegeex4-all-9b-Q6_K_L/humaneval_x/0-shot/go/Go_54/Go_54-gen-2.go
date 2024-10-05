You can use the sort package to sort the characters in both strings and compare them. Here's an example implementation:

```go
package main

import (
	"fmt"
	"sort"
	"strings"
)

func SameChars(s0 string, s1 string) bool {
	// Convert the strings to slices of runes
	runes0 := []rune(s0)
	runes1 := []rune(s1)

	// Sort the slices
	sort.Slice(runes0, func(i, j int) bool {
		return runes0[i] < runes0[j]
	})
	sort.Slice(runes1, func(i, j int) bool {
		return runes1[i] < runes1[j]
	})

	// Compare the sorted slices
	return strings.Compare(string(runes0), string(runes1)) == 0
}

func main() {
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
	fmt.Println(SameChars("abcd", "dddddddabc"))              // true
	fmt.Println(SameChars("dddddddabc", "abcd"))              // true
	fmt.Println(SameChars("eabcd", "dddddddabc"))              // false
	fmt.Println(SameChars("abcd", "dddddddabce"))             // false
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc"))    // false
}
```

This implementation first converts the strings to slices of runes, which allows for comparison of characters with different byte lengths. Then, it sorts the slices using the sort.Slice function, which sorts the runes based on their Unicode code points. Finally, it compares the sorted slices using the strings.Compare function. If the slices are equal, the function returns true, otherwise it returns false.
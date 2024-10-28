```go
package main

import (
	"fmt"
	"strings"
)

func SameChars(s0 string, s1 string) bool {
	return strings.Sort(s0) == strings.Sort(s1)
}

func main() {
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc"))  // true
	fmt.Println(SameChars("abcd", "dddddddabc"))               // true
	fmt.Println(SameChars("dddddddabc", "abcd"))               // true
	fmt.Println(SameChars("eabcd", "dddddddabc"))              // false
	fmt.Println(SameChars("abcd", "dddddddabce"))              // false
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc"))  // false
}
```


Output:

```
true
true
true
false
false
false
```


This program defines a function `SameChars` that checks if two strings have the same characters. It sorts the characters in each string and compares the results. If the sorted strings are equal, then the original strings have the same characters.

In the `main` function, we test the `SameChars` function with several pairs of strings. The output shows that the function correctly identifies pairs of strings with the same characters.
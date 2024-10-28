To split the given string of words on whitespace, if no whitespaces exist in the text, you should split on commas. If no commas exist in the string, you should return the number of lowercase letters with odd order in the alphabet (ord('a') = 0, ord('b') = 1, ... ord('z') = 25). The examples below illustrate these conditions.

Examples:

```go
SplitWords("Hello world!") ➞ ["Hello", "world!"]
SplitWords("Hello,world!") ➞ ["Hello", "world!"]
SplitWords("abcdef") == 3
```

To solve this problem, you can use the `strings.Fields` function, which splits the given string into a slice of substrings at each whitespace. If no whitespaces exist in the string, you can use the `strings.Fields` function again, this time splitting on commas. If no whitespaces or commas exist in the string, you can count the number of lowercase letters with odd order in the alphabet using a loop and the `unicode` package.

Here's an example solution in Go:

```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func SplitWords(txt string) interface{} {
	fields := strings.Fields(txt)
	if len(fields) > 0 {
		return fields
	}
	fields = strings.Fields(txt)
	if len(fields) > 0 {
		return fields
	}

	count := 0
	for _, char := range txt {
		if unicode.IsLower(char) && char%2 == 1 {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(SplitWords("Hello world!")) // ["Hello", "world!"]
	fmt.Println(SplitWords("Hello,world!")) // ["Hello", "world!"]
	fmt.Println(SplitWords("abcdef")) // 3
}
```

In this solution, the `SplitWords` function takes
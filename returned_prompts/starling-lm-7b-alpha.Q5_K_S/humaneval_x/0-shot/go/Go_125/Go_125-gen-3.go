To solve this problem, we can follow the steps below:

1. Check if the input string contains whitespace characters. If it does, split the string on whitespace and return the result.
2. If the string does not contain whitespace characters, check if it contains commas. If it does, split the string on commas and return the result.
3. If the string does not contain whitespace characters or commas, check the number of lowercase letters with odd order in the alphabet (a, c, e, ...). Calculate the count of these letters in the input string and return the count.
4. If none of the above conditions are met, return an error or an empty result, depending on your requirements.

Here's a possible implementation of the solution in Go:

```go
package main

import (
	"fmt"
	"strings"
)

func SplitWords(txt string) interface{} {
	// Check if the string contains whitespace characters
	if strings.ContainsAny(txt, " ") {
		return strings.Fields(txt)
	}
	// Check if the string contains commas
	if strings.ContainsAny(txt, ",") {
		return strings.Fields(txt)
	}
	// Count the number of lowercase letters with odd order in the alphabet
	count := 0
	for _, char := range txt {
		if char >= 'a' && char <= 'z' && (char-'a')%2 == 1 {
			count++
		}
	}
	return count
}
```

You can test the function with the provided examples:

```go
fmt.Println(SplitWords("Hello world!")) // Output: ["Hello", "world!"]
fmt.Println(SplitWords("Hello,world!")) // Output: ["Hello", "world!"]
fmt.Println(SplitWords("abcdef")) // Output: 3
```

In this implementation, the `SplitWords` function uses the `strings.ContainsAny` function to check if the input string contains whitespace characters or commas. It then uses the `strings.Fields` function to split the string based on whitespace or commas. If neither whitespace
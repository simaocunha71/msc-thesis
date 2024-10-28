Here is a simple solution using the `strings` package in Go:
```go
package main

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	// Convert the string to lowercase to ignore case
	str = strings.ToLower(str)

	// Create a set to store unique characters
	charSet := make(map[rune]bool)

	// Iterate over the string and add each character to the set
	for _, char := range str {
		if _, ok := charSet[char]; !ok {
			charSet[char] = true
		}
	}

	// Return the size of the set, which represents the number of distinct characters
	return len(charSet)
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
	fmt.Println(CountDistinctCharacters("Jerry")) // Output: 4
}
```
Explanation:

1. We convert the input string to lowercase using `strings.ToLower` to ignore case.
2. We create a `map[rune]bool` to store unique characters. The `rune` type is used to represent Unicode code points, and the `bool` value is used to indicate whether the character is present in the set.
3. We iterate over the string using a range loop, and for each character, we check if it's already present in the set using the `_, ok := charSet[char]` syntax. If it's not present, we add it to the set.
4. Finally, we return the size of the set, which represents the number of distinct characters in the input string.

You can test this function with different inputs to see that it correctly counts the number of distinct characters. For example, `CountDistinctCharacters("xyzXYZ")` returns 3, and `CountDistinctCharacters("Jerry")` returns 4.
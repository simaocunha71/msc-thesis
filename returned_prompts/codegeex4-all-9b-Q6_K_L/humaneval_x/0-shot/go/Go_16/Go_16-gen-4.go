To solve this problem, we need to iterate over the string, convert each character to its lowercase equivalent, and then count the number of distinct characters. Here's one way to implement this in Go:

```go
package main

import (
	"fmt"
	"strings"
)

// CountDistinctCharacters counts the number of distinct characters in a string, regardless of case
func CountDistinctCharacters(str string) int {
	// Convert the string to lowercase
	str = strings.ToLower(str)

	// Create a map to keep track of the distinct characters
	distinctChars := make(map[rune]bool)

	// Iterate over the string and add each character to the map
	for _, char := range str {
		distinctChars[char] = true
	}

	// Return the number of distinct characters
	return len(distinctChars)
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // 3
	fmt.Println(CountDistinctCharacters("Jerry"))  // 4
}
```

In this code, we first convert the input string to lowercase using the `strings.ToLower` function. Then, we create a map to keep track of the distinct characters. We iterate over the string and add each character to the map. Since a map only allows unique keys, any duplicate character will not be added to the map. Finally, we return the number of keys in the map, which represents the number of distinct characters in the string.
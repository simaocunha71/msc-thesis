To solve this problem, we can follow the steps below:

1. Replace all spaces in the string with underscores.
2. Replace all consecutive spaces with a single space.
3. Replace all spaces that are at the beginning or end of the string with underscores.
4. Replace all spaces that are between two non-space characters with underscores.
5. If the string has more than 2 consecutive spaces, then replace them with a single space.
6. Return the modified string.

Here is an example of how to implement this in Go:

```go
package main

import (
	"fmt"
	"strings"
)

func FixSpaces(text string) string {
	// Replace all spaces with underscores
	text = strings.ReplaceAll(text, " ", "_")

	// Replace all consecutive spaces with a single space
	text = strings.ReplaceAll(text, "  ", "-")

	// Replace spaces at the beginning and end of the string with underscores
	text = strings.TrimSpace(text)

	// Replace spaces between two non-space characters with underscores
	text = strings.ReplaceAll(text, "_ ", "_")

	return text
}

func main() {
	fmt.Println(FixSpaces("Example"))           // "Example"
	fmt.Println(FixSpaces("Example 1"))         // "Example_1"
	fmt.Println(FixSpaces(" Example 2"))        // "_Example_2"
	fmt.Println(FixSpaces(" Example   3"))      // "_Example-3"
	fmt.Println(FixSpaces("Example     4"))     // "_Example-4"
	fmt.Println(FixSpaces("Example     4    ")) // "_Example-4"
}
```

In this code, we use the `strings` package to perform the string manipulations. The `ReplaceAll` function is used to replace all occurrences of a substring with another substring. The `TrimSpace` function is used to remove any leading or trailing spaces from the string.

The `FixSpaces` function follows the steps outlined above to replace the spaces in the input
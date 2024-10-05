The question is asking us to write a function that accepts a list of strings and returns the string with the maximum number of unique characters. If there are multiple strings with the same number of unique characters, we need to return the one that comes first in lexicographical order.

Here is a possible solution in Go:

```go
package main

import (
	"fmt"
	"sort"
	"strings"
)

func FindMax(words []string) string {
	// Sort the words in lexicographical order
	sort.Strings(words)

	// Initialize variables to keep track of the maximum number of unique characters and the corresponding word
	maxUniqueChars := 0
	maxWord := ""

	// Iterate over the words and count the number of unique characters in each word
	for _, word := range words {
		uniqueChars := make(map[rune]bool)
		for _, char := range word {
			uniqueChars[char] = true
		}

		// If the current word has more unique characters than the maximum, update the maximum and the corresponding word
		if len(uniqueChars) > maxUniqueChars {
			maxUniqueChars = len(uniqueChars)
			maxWord = word
		}
	}

	return maxWord
}

func main() {
	fmt.Println(FindMax([]string{"name", "of", "string"})) // Output: "string"
	fmt.Println(FindMax([]string{"name", "enam", "game"})) // Output: "enam"
	fmt.Println(FindMax([]string{"aaaaaaa", "bb", "cc"})) // Output: "aaaaaaa"
}
```

Explanation:
1. We start by sorting the words in lexicographical order using the `sort.Strings()` function.
2. We initialize two variables: `maxUniqueChars` to keep track of the maximum number of unique characters and `maxWord` to keep track of the corresponding word.
3. We iterate over the words and for each word, we create a map `uniqueChars` to store the unique characters.
4. For each character in the word, we check if it is already present in the `uniqueChars` map. If it is not present, we add it to the map.
5. After counting the number of unique characters in the word, we compare it with the current maximum number of unique characters. If it is greater, we update the maximum and the corresponding word.
6. Finally, we return the word with the maximum number of unique characters.
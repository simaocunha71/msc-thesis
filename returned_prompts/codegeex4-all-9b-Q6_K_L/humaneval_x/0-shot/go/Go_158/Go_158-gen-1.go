You can solve this problem by using a map to count the number of unique characters in each word and then sorting the words based on this count and lexicographical order. Here is a simple solution in Go:

```go
import (
	"sort"
	"strings"
)

func FindMax(words []string) string {
	// Count unique characters in each word
	counts := make([]int, len(words))
	for i, word := range words {
		seen := make(map[rune]bool)
		for _, c := range word {
			if !seen[c] {
				seen[c] = true
				counts[i]++
			}
		}
	}

	// Sort words based on unique character count and lexicographical order
	sort.Slice(words, func(i, j int) bool {
		if counts[i] != counts[j] {
			return counts[i] > counts[j]
		}
		return words[i] < words[j]
	})

	// Return the first word in the sorted list
	return words[0]
}
```

This solution first counts the number of unique characters in each word and stores these counts in a slice. Then it sorts the words based on the counts and lexicographical order. Finally, it returns the first word in the sorted list, which is the word with maximum number of unique characters. If there are multiple words with the same number of unique characters, the one which comes first in lexicographical order is returned.
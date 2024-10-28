```go
import (
	"strings"
)

func Histogram(test string) map[rune]int {
	if len(test) == 0 {
		return map[rune]int{}
	}
	counts := make(map[rune]int)
	words := strings.Fields(test)
	for _, word := range words {
		for _, letter := range word {
			counts[letter]++
		}
	}
	maxCount := 0
	for _, count := range counts {
		if count > maxCount {
			maxCount = count
		}
	}
	result := make(map[rune]int)
	for letter, count := range counts {
		if count == maxCount {
			result[letter] = count
		}
	}
	return result
}
```

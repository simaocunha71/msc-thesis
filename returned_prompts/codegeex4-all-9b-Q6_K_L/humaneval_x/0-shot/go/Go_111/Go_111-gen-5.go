```go
import (
	"strings"
	"unicode"
)

func Histogram(test string) map[rune]int {
	counts := make(map[rune]int)
	for _, c := range test {
		if !unicode.IsLetter(c) {
			continue
		}
		c = unicode.ToLower(c)
		counts[c]++
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
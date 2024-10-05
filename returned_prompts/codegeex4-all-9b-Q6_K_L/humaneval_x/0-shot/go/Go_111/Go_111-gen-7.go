```go
import (
	"strings"
)

func Histogram(test string) map[rune]int {
    counts := make(map[rune]int)
    for _, char := range strings.Fields(test) {
        counts[rune(char[0])]++
    }
    maxCount := 0
    for _, count := range counts {
        if count > maxCount {
            maxCount = count
        }
    }
    result := make(map[rune]int)
    for char, count := range counts {
        if count == maxCount {
            result[char] = count
        }
    }
    return result
}
```

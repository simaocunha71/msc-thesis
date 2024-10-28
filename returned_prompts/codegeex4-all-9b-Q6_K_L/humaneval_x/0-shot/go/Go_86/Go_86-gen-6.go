Here's one way you can solve this problem in Go:

```go
import (
    "sort"
    "strings"
)

func AntiShuffle(s string) string {
    words := strings.Fields(s)
    for i, word := range words {
        runes := []rune(word)
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        words[i] = string(runes)
    }
    return strings.Join(words, " ")
}
```

In this solution, we first split the input string into words using `strings.Fields(s)`. Then, for each word, we convert it to a slice of runes using `[]rune(word)`. We sort this slice using `sort.Slice` with a custom comparator function that compares two runes based on their ASCII values. Finally, we convert the sorted runes back to a string and replace the original word with it. Finally, we join the words back together using `strings.Join(words, " ")` to produce the final result.
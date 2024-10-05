Here is the solution in Go:

```go
import (
    "sort"
    "strings"
)

func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    result := ""
    for _, word := range words {
        chars := []rune(word)
        sort.Runes(chars)
        result += string(chars) + " "
    }
    return strings.TrimSpace(result)
}
```

In this solution, we first split the input string into words using the `strings.Split` function. Then, for each word, we convert it to a slice of runes (a Unicode code point), sort the slice using the `sort.Runes` function, and then convert the slice back to a string. We append each sorted word to the result string, followed by a space. Finally, we use the `strings.TrimSpace` function to remove any trailing spaces from the result string.
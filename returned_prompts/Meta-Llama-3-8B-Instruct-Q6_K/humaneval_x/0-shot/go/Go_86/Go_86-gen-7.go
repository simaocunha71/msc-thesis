Here is the solution in Go:

```go
import (
    "sort"
    "strings"
)

func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    result := []string{}
    for _, word := range words {
        letters := []rune(word)
        sort.Runes(letters)
        result = append(result, string(letters))
    }
    return strings.Join(result, " ")
}
```

This function splits the input string into words, sorts each word's letters in ascending order, and then joins the words back together with spaces in between. The `sort.Runes` function is used to sort the letters of each word. The `strings.Split` function is used to split the input string into words, and the `strings.Join` function is used to join the words back together. The result is the ordered version of the input string.
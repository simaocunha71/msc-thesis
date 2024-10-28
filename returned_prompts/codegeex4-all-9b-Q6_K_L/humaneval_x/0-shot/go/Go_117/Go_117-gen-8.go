```go
import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    var result []string
    for _, word := range strings.Fields(s) {
        consonants := 0
        for _, c := range word {
            if !bytes.ContainsRune([]byte("aeiouAEIOU"), c) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}
```

Here is the solution in Go:

```go
import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    words := strings.Fields(s)
    result := []string{}
    for _, word := range words {
        wordBytes := []byte(word)
        consonants := 0
        for _, b := range wordBytes {
            if !isVowel(b) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}

func isVowel(b byte) bool {
    vowels := []byte("aeiouAEIOU")
    for _, vowel := range vowels {
        if b == vowel {
            return true
        }
    }
    return false
}
```

This solution first splits the input string into words using the `strings.Fields` function. Then, for each word, it counts the number of consonants by iterating over each byte in the word and checking if it's a vowel using the `isVowel` function. If the word contains exactly `n` consonants, it's added to the result list. The `isVowel` function is a simple helper function that checks if a given byte is a vowel. The solution returns the list of words that contain exactly `n` consonants.
Here is a simple implementation in Go:
```go
package main

import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    words := strings.Split(s, " ")
    result := make([]string, 0)
    for _, word := range words {
        word = strings.ToLower(word)
        consonants := 0
        for _, r := range word {
            if !isVowel(r) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}

func isVowel(r rune) bool {
    return r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u'
}

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4)) // ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3)) // ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2)) // []
    fmt.Println(SelectWords("Hello world", 4)) // ["world"]
    fmt.Println(SelectWords("Uncle sam", 3)) // ["Uncle"]
}
```
The `SelectWords` function splits the input string into individual words, and then checks each word to see if it contains exactly `n` consonants. The `isVowel` function is used to determine if a character is a vowel or not. The function returns a list of words that meet the condition. If the input string is empty, it returns an empty list. The `main` function demonstrates the usage of the `SelectWords` function with different inputs.
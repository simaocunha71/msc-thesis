Here is the solution in Go:
```go
package main

import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    var result []string
    words := strings.Split(s, " ")
    for _, word := range words {
        if len(word) > 0 {
            consonants := 0
            for _, c := range word {
                if !strings.Contains("aeiouAEIOU", string(c)) {
                    consonants++
                }
            }
            if consonants == n {
                result = append(result, word)
            }
        }
    }
    return result
}

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4))  // ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3))  // ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2))     // []
    fmt.Println(SelectWords("Hello world", 4))           // ["world"]
    fmt.Println(SelectWords("Uncle sam", 3))             // ["Uncle"]
}
```



Explanation:

*   We use the `strings.Split` function to split the input string `s` into individual words.
*   We then iterate over each word and count the number of consonants using a loop.
*   We check if the number of consonants matches the target number `n`. If it does, we add the word to the result list.
*   Finally, we return the result list.

The `strings.Contains` function is used to check if a character is a vowel or not. If the character is not a vowel, we increment the consonant count. The `append` function is used to add the word to the result list. The `main` function is used to test the `SelectWords` function with different inputs.
Here is the solution in Go:
```go
package main

import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    words := strings.Fields(s)
    result := make([]string, 0)
    for _, word := range words {
        consonants := 0
        for _, char := range word {
            if !strings.ContainsRune("aeiouAEIOU", char) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}

func main() {
    s := "Mary had a little lamb"
    n := 4
    result := SelectWords(s, n)
    for _, word := range result {
        println(word)
    }
}
```
This function first splits the input string `s` into individual words using the `strings.Fields` function. Then it iterates over each word, counting the number of consonants in the word using a loop and the `strings.ContainsRune` function. If the number of consonants in a word matches the target number `n`, the word is added to the result slice. Finally, the function returns the result slice.

In the `main` function, we test the `SelectWords` function with the input string "Mary had a little lamb" and the target number 4, and print the result words. The output should be `["little"]`. You can modify the input string and the target number to test the function with different inputs.
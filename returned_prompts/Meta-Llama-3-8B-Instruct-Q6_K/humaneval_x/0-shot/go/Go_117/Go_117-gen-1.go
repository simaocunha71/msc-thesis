Here is the solution to the problem:

```go
package main

import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    words := strings.Split(s, " ")
    var result []string
    var consonants int

    for _, word := range words {
        for _, char := range word {
            if !isVowel(char) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
        consonants = 0
    }

    return result
}

func isVowel(char byte) bool {
    char = byte(strings.ToLower(string(char)))
    return char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u'
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

This program defines a function `SelectWords` that takes a string `s` and an integer `n` as input, and returns a slice of strings that contain exactly `n` consonants. The function works by splitting the input string into individual words, and then iterating over each word to count the number of consonants. If the count matches `n`, the word is added to the result slice. Finally, the function returns the result slice.

The `isVowel` function is a helper function that checks whether a given character is a vowel or not. It converts the character to lowercase and then checks if it is one of the vowels 'a', 'e', 'i', 'o', or 'u'.

In the `main` function, we test the `SelectWords` function with the input string "Mary had a little lamb" and `n = 4`, and print the result. The output should be "little". You can modify the input string and `n` to test the function with different inputs.
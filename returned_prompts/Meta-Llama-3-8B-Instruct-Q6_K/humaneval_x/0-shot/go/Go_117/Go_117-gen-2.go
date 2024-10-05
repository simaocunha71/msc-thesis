Here is the solution in Go:
```go
package main

import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    words := strings.Split(s, " ")
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
    return b == 'a' || b == 'e' || b == 'i' || b == 'o' || b == 'u' ||
        b == 'A' || b == 'E' || b == 'I' || b == 'O' || b == 'U'
}

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4))  // ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3))  // ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2))      // []
    fmt.Println(SelectWords("Hello world", 4))            // ["world"]
    fmt.Println(SelectWords("Uncle sam", 3))              // ["Uncle"]
}
```
This solution splits the input string into individual words and then iterates over each word to count the number of consonants. It uses a helper function `isVowel` to check if a character is a vowel or not. If the number of consonants in a word matches the given `n`, the word is added to the result slice. Finally, the function returns the list of words that contain exactly `n` consonants. 

Note: The `main` function is added to test the `SelectWords` function with different inputs. The `fmt.Println` statements print the output of each function call. You can run this code to see the output. 

Also, note that this solution considers only the letters 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' as vowels. If you want to consider other characters as vowels, you can modify the `isVowel` function accordingly. 

This solution has a time complexity of O
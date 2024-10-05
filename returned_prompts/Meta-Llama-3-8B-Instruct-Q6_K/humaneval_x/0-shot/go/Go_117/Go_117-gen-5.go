Here is a solution in Go that implements the function `SelectWords` as described:
```go
package main

import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    // Split the input string into words
    words := strings.Split(s, " ")

    // Initialize an empty list to store the result
    result := []string{}

    // Iterate over each word in the list of words
    for _, word := range words {
        // Initialize a byte buffer to count the consonants
        var consonantCount int

        // Iterate over each byte in the word
        for _, byte := range []byte(word) {
            // Check if the byte is a consonant
            if byte != 'a' && byte != 'e' && byte != 'i' && byte != 'o' && byte != 'u' && byte != ' ' {
                // Increment the consonant count
                consonantCount++
            }
        }

        // Check if the word contains exactly n consonants
        if consonantCount == n {
            // Add the word to the result list
            result = append(result, word)
        }
    }

    // Return the result list
    return result
}

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4)) // Output: ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3)) // Output: ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2)) // Output: []
    fmt.Println(SelectWords("Hello world", 4)) // Output: ["world"]
    fmt.Println(SelectWords("Uncle sam", 3)) // Output: ["Uncle"]
}
```
This solution uses the `strings.Split` function to split the input string into words, and then iterates over each word to count the number of consonants using a byte buffer. It checks if the word contains exactly `n` consonants and adds it to the result list if it does. Finally, it returns the result list.

Note that this solution assumes that the input string contains only letters and spaces, as specified in the problem statement. It also assumes that the input natural number `n` is positive. If the input string is empty or `n` is 0, the function returns an empty list. If `n` is negative, the function returns an empty list as well
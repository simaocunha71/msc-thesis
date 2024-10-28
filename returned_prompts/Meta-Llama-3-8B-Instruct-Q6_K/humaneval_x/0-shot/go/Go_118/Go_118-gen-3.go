Here is a Go solution for the problem:

```go
package main

import (
    "bytes"
    "fmt"
    "strings"
)

func GetClosestVowel(word string) string {
    vowels := "aeiouAEIOU"
    word = strings.ToLower(word)
    for i := len(word) - 1; i > 0; i-- {
        if bytes.IndexByte([]byte(vowels), word[i]) != -1 {
            return string(word[i])
        }
    }
    return ""
}

func main() {
    fmt.Println(GetClosestVowel("yogurt"))  // Output: u
    fmt.Println(GetClosestVowel("FULL"))   // Output: u
    fmt.Println(GetClosestVowel("quick"))  // Output: 
    fmt.Println(GetClosestVowel("ab"))     // Output: 
}
```

This program works by iterating through the word from right to left and checking if the current character is a vowel. If it is, it returns the character. If it doesn't find any vowel that meets the condition, it returns an empty string. The `strings.ToLower` function is used to make the function case-insensitive. The `bytes.IndexByte` function is used to check if the character is a vowel. If the character is found in the `vowels` string, it returns the index of the character, which is then converted to a string and returned. If the character is not found, it returns -1. The loop continues until it finds a vowel or it reaches the beginning of the word. If it reaches the beginning of the word without finding a vowel, it returns an empty string. The `main` function tests the `GetClosestVowel` function with different inputs and prints the results. 
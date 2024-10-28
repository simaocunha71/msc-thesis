
// Check if the given string is a palindrome
func IsPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-i-1] {
            return false
        }
    }
    return true
}

// This function works by comparing the first and last characters of the string, then the second and second last characters, and so on.
// If any of these pairs of characters do not match, the function returns false, indicating that the string is not a palindrome.
// If the function has checked all the pairs of characters and found no mismatches, it returns true, indicating that the string is a palindrome.

```

## 2.2.3. Exercises

1. Write a function that counts the number of vowels in a given string.

```go
package main

import (
    "fmt"
    "strings"
)

func CountVowels(text string) int {
    count := 0
    text = strings.ToLower(text)
    for _, char := range text {
        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(CountVowels("Hello, World!"))  // Output: 3
    fmt.Println(CountVowels("aeiouAEIOU"))  // Output: 10
}
```

2. Write a function that checks if a given string is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once.

```go
package main

import (
    "fmt"
    "strings"
)

func IsPangram(text string) bool {
    alphabet := "abcdefghijklmnopqrstuvwxyz"

    for _, char := range alphabet {
        if !strings.ContainsRune(strings.ToLower(text), char) {
            return false
       
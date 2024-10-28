Here is the solution in Go:

```go
package main

import (
    "strings"
)

// Create a function Encrypt that takes a string as an argument and
// returns a string Encrypted with the alphabet being rotated.
// The alphabet should be rotated in a manner such that the letters
// shift down by two multiplied to two places.
// For example:
// Encrypt('hi') returns 'lm'
// Encrypt('asdfghjkl') returns 'ewhjklnop'
// Encrypt('gf') returns 'kj'
// Encrypt('et') returns 'ix'
func Encrypt(s string) string {
    // Define the alphabet
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    // Convert the string to lowercase
    s = strings.ToLower(s)
    // Create a new string to store the encrypted result
    result := ""
    // Iterate over each character in the string
    for _, char := range s {
        // Check if the character is a letter
        if alphabetIndex := strings.Index(alphabet, string(char)); alphabetIndex != -1 {
            // Calculate the new index by shifting down by 4 places
            newAlphabetIndex := (alphabetIndex + 4) % len(alphabet)
            // Append the character at the new index to the result
            result += string(alphabet[newAlphabetIndex])
        } else {
            // If the character is not a letter, just append it to the result
            result += string(char)
        }
    }
    // Return the encrypted result
    return result
}

func main() {
    // Test the function
    fmt.Println(Encrypt("hi"))  // Output: lm
    fmt.Println(Encrypt("asdfghjkl"))  // Output: ewhjklnop
    fmt.Println(Encrypt("gf"))  // Output: kj
    fmt.Println(Encrypt("et"))  // Output: ix
}
```

This function works by iterating over each character in the input string. If the character is a letter, it calculates the new index by shifting down by 4 places and appends the character at the new index to the result. If the character is not a letter, it just appends it to the result. The function then returns the encrypted result. The `strings.Index` function is used to find the index of a character in the alphabet, and the `%` operator is used to ensure that the new index is within the bounds of the alphabet. The `strings.ToLower` function is used to convert the input string
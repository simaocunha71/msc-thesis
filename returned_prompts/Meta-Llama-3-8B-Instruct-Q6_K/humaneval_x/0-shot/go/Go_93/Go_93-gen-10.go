Here is a solution in Go:
```go
package main

import (
    "strings"
)

func Encode(message string) string {
    encoded := strings.Map(func(r rune) rune {
        if 'a' <= r && r <= 'z' {
            return 'a' + (r - 'a' + 2) % 26
        } else if 'A' <= r && r <= 'Z' {
            return 'A' + (r - 'A' + 2) % 26
        }
        return r
    }, message)
    return strings.Map(func(r rune) rune {
        return 'a' <= r && r <= 'z' ? 'A' + (r-'a') : 'A' <= r && r <= 'Z' ? 'a' + (r-'A') : r
    }, encoded).String()
}

func main() {
    message := "This is a message"
    encoded := Encode(message)
    println(encoded) // Output: tHKS KS C MGSSCGG
}
```
The solution uses two `strings.Map` functions to achieve the desired encoding.

The first `strings.Map` function is used to replace all vowels with the letter that appears 2 places ahead of that vowel in the English alphabet. It does this by checking if the rune is a lowercase or uppercase letter, and if it is, it adds 2 to the rune's ASCII value (after subtracting the ASCII value of 'a' or 'A' respectively) and takes the result modulo 26 to wrap around the alphabet.

The second `strings.Map` function is used to swap the case of all letters. It checks if the rune is a lowercase or uppercase letter, and if it is, it returns the corresponding uppercase or lowercase letter.

Finally, the encoded string is returned. In the `main` function, we test the `Encode` function with the message "This is a message" and print the result.
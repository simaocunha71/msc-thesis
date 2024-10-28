Here is the solution:
```go
package main

import (
    "strings"
)

func Encrypt(s string) string {
    // Convert the string to a byte slice
    b := []byte(s)
    // Define the alphabet
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    // Rotate the alphabet by 4 places (2*2)
    rotatedAlphabet := alphabet[4:] + alphabet[:4]
    // Create a mapping from the original alphabet to the rotated one
    mapping := make(map[rune]rune)
    for i, c := range alphabet {
        mapping[rune(alphabet[i])] = rune(rotatedAlphabet[i])
    }
    // Replace each character in the input string with its corresponding rotated character
    for i := range b {
        if b[i] >= 'a' && b[i] <= 'z' {
            b[i] = mapping[rune(b[i])]
        }
    }
    // Convert the byte slice back to a string
    return string(b)
}

func main() {
    s := "hi"
    result := Encrypt(s)
    println(result)  // Output: lm
}
```
The solution works by first converting the input string to a byte slice. It then defines the original alphabet and rotates it by 4 places (2*2). A mapping is created from the original alphabet to the rotated one. The function then iterates over the input string, replacing each character with its corresponding rotated character using the mapping. Finally, the byte slice is converted back to a string and returned. The `main` function demonstrates the usage of the `Encrypt` function.
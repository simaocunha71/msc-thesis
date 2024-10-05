```go
package main

import (
    "fmt"
)

// returns encoded string by shifting every character by 5 in the alphabet.
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
        } else if ch >= 'A' && ch <= 'Z' {
            newRunes = append(newRunes, (ch+5-'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

// takes as input string encoded with EncodeShift function. Returns decoded string.
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch-5-'a')%26+'a')
        } else if ch >= 'A' && ch <= 'Z' {
            newRunes = append(newRunes, (ch-5-'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

func main() {
    s := "Hello, World!"
    encoded := EncodeShift(s)
    fmt.Println("Encoded:", encoded)
    decoded := DecodeShift(encoded)
    fmt.Println("Decoded:", decoded)
}
```

This code defines two functions, `EncodeShift` and `DecodeShift`, which are used to shift every character in a string by 5 positions in the alphabet. The `EncodeShift` function takes a string as input and returns the encoded string, while the `DecodeShift` function takes an encoded string as input and returns the decoded string.

The `EncodeShift` function works by iterating over each character in the input string. If the character is a lowercase letter, it shifts it by 5 positions in the alphabet using the formula `(ch+5-'a')%26+'a'`. If the character is an uppercase letter, it shifts it by 5 positions in the alphabet using the formula `(ch+5
The provided solution is missing the decoding part. Here is the complete solution with both encoding and decoding functions:

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
        if 'a' <= ch && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
        } else if 'A' <= ch && ch <= 'Z' {
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
        if 'a' <= ch && ch <= 'z' {
            newRunes = append(newRunes, (ch-5-'a')%26+'a')
        } else if 'A' <= ch && ch <= 'Z' {
            newRunes = append(newRunes, (ch-5-'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

func main() {
    s := "hello"
    encoded := EncodeShift(s)
    fmt.Println("Encoded:", encoded)
    decoded := DecodeShift(encoded)
    fmt.Println("Decoded:", decoded)
}
```

The `EncodeShift` function shifts each character in the input string by 5 positions in the alphabet. If the character is not a letter, it remains unchanged. The `DecodeShift` function does the opposite, shifting each character by 5 positions in the opposite direction. The modulo operator `%26` is used to wrap around the alphabet, so that characters at the end of the alphabet (e.g., 'z' or 'Z') are shifted to the beginning. The `main` function demonstrates the encoding and decoding of a sample string.
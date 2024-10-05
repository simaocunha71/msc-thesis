```go
package main

import (
    "fmt"
    "strings"
)

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
    s := "hello world"
    encoded := EncodeShift(s)
    fmt.Println("Encoded:", encoded)
    decoded := DecodeShift(encoded)
    fmt.Println("Decoded:", decoded)
}
```

The `EncodeShift` function takes a string `s` as input, and for each character in the string, it checks if it's a lowercase letter, an uppercase letter, or a non-alphabetic character. If it's a lowercase letter, it shifts it 5 positions forward in the alphabet using the formula `(ch+5-'a')%26+'a'`. If it's an uppercase letter, it shifts it 5 positions forward using the formula `(ch+5-'A')%26+'A'`. If it's a non-alphabetic character, it leaves it unchanged. The function returns the encoded string.

The `DecodeShift` function is similar to `EncodeShift`, but it shifts the characters 5 positions backward in the alphabet instead of forward. It uses the formula `(ch-5-'a')%26+'
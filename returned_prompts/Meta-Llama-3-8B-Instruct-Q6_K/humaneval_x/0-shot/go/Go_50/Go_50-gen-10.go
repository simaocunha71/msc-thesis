The provided solution is in Go programming language. Here is a breakdown of the code:

1. The `EncodeShift` function takes a string `s` as input and returns an encoded string by shifting every character by 5 in the alphabet. It does this by iterating over each rune in the input string, adding 5 to its ASCII value, taking the remainder modulo 26 to wrap around to the beginning of the alphabet, and appending the resulting rune to a new slice.

2. The `DecodeShift` function takes an encoded string as input and returns the decoded string. It does this by iterating over each rune in the input string, subtracting 5 from its ASCII value, taking the remainder modulo 26 to wrap around to the beginning of the alphabet, and appending the resulting rune to a new slice.

Here is the corrected code:

```go
package main

import (
    "fmt"
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
    s := "Hello, World!"
    encoded := EncodeShift(s)
    fmt.Println("Encoded:", encoded)
    decoded := DecodeShift(encoded)
    fmt.Println("Decoded:", decoded)
}
```

In this corrected code,
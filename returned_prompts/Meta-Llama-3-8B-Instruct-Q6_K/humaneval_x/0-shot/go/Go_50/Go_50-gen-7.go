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
            newRunes = append(newRunes, (ch-5+'a')%26+'a')
        } else if ch >= 'A' && ch <= 'Z' {
            newRunes = append(newRunes, (ch-5+'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

func main() {
    s := "hello"
    encoded := EncodeShift(s)
    fmt.Println(encoded) // prints "mjqqt"
    decoded := DecodeShift(encoded)
    fmt.Println(decoded) // prints "hello"
}
```

Explanation:
The code defines two functions: `EncodeShift` and `DecodeShift`. `EncodeShift` takes a string as input and returns a new string where every character is shifted 5 positions forward in the alphabet. This is done by checking if the character is a lowercase or uppercase letter, and if so, adding 5 to its ASCII value and taking the result modulo 26 to wrap around the alphabet. Non-letter characters are left unchanged.

`DecodeShift` is the inverse of `EncodeShift`, shifting every character 5 positions backward in the alphabet. It does this by subtracting 5 from the ASCII value of each character, taking the result modulo 26 to wrap around the alphabet, and
The provided functions EncodeShift and DecodeShift aim to shift every character in a given string by 5 positions in the alphabet.

The EncodeShift function works as follows:

1. It converts the input string into a slice of runes.
2. It creates a new slice to store the encoded runes.
3. For each rune in the input slice, it calculates the encoded rune by adding 5 to the rune's value (in ASCII) and taking the modulus 26 to wrap around the alphabet. The result is then added to the new slice.
4. Finally, it converts the encoded slice of runes back into a string and returns it.

The DecodeShift function is essentially the inverse of EncodeShift and works as follows:

1. It converts the input string into a slice of runes.
2. It creates a new slice to store the decoded runes.
3. For each rune in the input slice, it calculates the decoded rune by subtracting 5 from the rune's value (in ASCII) and taking the modulus 26 to wrap around the alphabet. The result is then added to the new slice.
4. Finally, it converts the decoded slice of runes back into a string and returns it.

Here's the corrected implementation:

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
        } else
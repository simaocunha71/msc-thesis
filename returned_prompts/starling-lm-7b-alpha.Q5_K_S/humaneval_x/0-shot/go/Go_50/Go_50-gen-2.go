    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5+26)%26)
    }
    return string(newRunes)
}

In the above code, the function EncodeShift(s string) returns an encoded string by shifting every character by 5 in the alphabet. Similarly, the function DecodeShift(s string) takes as input string encoded with EncodeShift function and returns the decoded string. However, the code you've written is incorrect. Here's the corrected code:

func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if ch >= 'a' && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
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
            newRunes = append(newRunes, (ch-5+26)%26+'a')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

In the corrected code, the EncodeShift and DecodeShift functions now correctly handle uppercase letters and non-alphabetic characters by appending them without any change.

To test the functions, you can use the following code:

package main

import "fmt"

func main() {
    s := "Hello World"
    encoded := EncodeShift(s)
    fmt.Println(encoded)
    decoded := DecodeShift(encoded)
    fmt.Println(decoded
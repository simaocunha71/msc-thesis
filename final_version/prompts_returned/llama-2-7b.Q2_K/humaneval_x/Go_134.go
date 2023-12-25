import (
    "strings"
)

// Create a function that returns true if the last character
// of a given string is an alphabetical character and is not
// a part of a word, and false otherwise.
// Note: "word" is a group of characters separated by space.
// 
// Examples:
// CheckIfLastCharIsALetter("apple pie") ➞ false
// CheckIfLastCharIsALetter("apple pi e") ➞ true
// CheckIfLastCharIsALetter("apple pi e ") ➞ false
// CheckIfLastCharIsALetter("") ➞ false
func CheckIfLastCharIsALetter(txt string) bool {
    if len(strings.TrimSpace(txt)) == 0 {
        return false
    } else if strings.ToLower(strings.TrimSpace(txt)[len(txt)-1:]) != "e" &&
               strings.ToLower(strings.TrimSpace(txt)[len(txt)-1:])...
               [0] == "a" {
        return true
    } else {
        return false
    }
}

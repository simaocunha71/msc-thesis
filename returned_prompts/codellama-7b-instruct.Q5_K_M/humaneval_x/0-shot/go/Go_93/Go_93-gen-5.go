import (
    "strings"
    "unicode"
)

// Write a function that takes a message, and Encodes in such a
// way that it swaps case of all letters, replaces all vowels in
// the message with the letter that appears 2 places ahead of that
// vowel in the english alphabet.
// Assume only letters.
// 
// Examples:
// >>> Encode('test')
// 'TGST'
// >>> Encode('This is a message')
// 'tHKS KS C MGSSCGG'
func Encode(message string) string {
    encoded := ""
    for _, char := range message {
        if unicode.IsLetter(char) {
            if unicode.IsUpper(char) {
                encoded += string(unicode.ToLower(char))
            } else {
                encoded += string(unicode.ToUpper(char))
            }
        } else {
            encoded += string(char)
        }
    }
    return encoded
}


B:
import (
    "strings"
)

// Write a function that takes a message, and Encodes in such a
// way that it swaps case of all letters, replaces all vowels in
// the message with the letter that appears 2 places ahead of that
// vowel in the english alphabet.
// Assume only letters.
// 
// Examples:
// >>> Encode('test')
// 'TGST'
// >>> Encode('This is a message')
// 'tHKS KS C MGSSCGG'
func Encode(message string) string {
    vowels := []rune("aeiou")
    encoded := ""
    for i, char := range message {
        if unicode.IsLetter(char) {
            if unicode.IsUpper(char) {
                encoded += string(unicode.ToLower(char))
            } else {
                encoded += string(unicode.ToUpper(char))
            }
        } else {
            encoded += string(char)
        }
        if unicode.IsLetter(char) {
            if strings.Contains(string(vowels), string(char
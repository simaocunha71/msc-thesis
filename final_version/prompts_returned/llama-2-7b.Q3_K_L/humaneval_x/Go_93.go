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
    // encode message in such a way that it swaps case of all letters, replaces
    // the vowels with the letter that appears two places ahead.
	// use regex to split strings by space and replace vowel
    
    var encoded = ""

    for i := 0; i < len(message); i++ {
        switch message[i] {
            case "a", "e", "i", "o", "u":
                if i > 0 && i != len(message) - 1 {
                    encoded += "(" + strings.ToUpper(string(message[i+2])) + ")"
                } else if i < (len(message) - 1) {
                    encoded += ("(" + string(message[i+1]) + ")")
                }
            default:
                encoded += message[i]
        }
    }
    return encoder
}
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
    var r, vowels = "aeiou"
    
    for char in strings.Split(message, ",") {
        if let c = char {
            char = strings.ToLower(char)
            
            switch strings.FindIndex(c, &r) {
                case -1:
                    return r + message
                default:
                    vowels = strings.Replace(vowels[strings.PositionInRange(&r, 2, strings.Len(message)-4)], "e", "")
            }
        } else if let i = strings.IndexOf(r, ",") {
            return r + message[:i] + r + message[strings.Len(message):strings.Len(message)+strings.Len(vowels)]
        } else 
        	return r + message
    }
}
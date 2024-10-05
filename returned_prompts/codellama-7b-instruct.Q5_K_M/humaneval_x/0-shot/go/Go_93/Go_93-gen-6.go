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

    // convert to upper case
    message = strings.ToUpper(message)

    // define a map for the vowels
    var vowelMap = map[string]string {
        "A": "C",
        "E": "G",
        "I": "K",
        "O": "S",
        "U": "V",
        "Y": "X",
    }

    // define a map for the vowel pairs
    var vowelPairMap = map[string]string {
        "A": "B",
        "E": "F",
        "I": "H",
        "O": "J",
        "U": "W",
        "Y": "Z",
    }

    // define a variable to hold the encoded string
    var encodedMessage string

    // loop through the message
    for _, character := range message {
        // if the character is a vowel
        if _, ok := vowelMap[string(character)]; ok {
            // replace with the vowel pair
            encodedMessage += vowelPairMap[string(character)]
        }
        // else
        else {
            // replace with the upper case character
            encodedMessage += string(character)
        }
    }

    // return the encoded message
    return encodedMessage
}


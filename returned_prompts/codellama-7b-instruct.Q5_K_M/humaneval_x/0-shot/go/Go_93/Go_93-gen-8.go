import (
    "strings"
)

// Write a function that takes a message, and Encodes in such a
// way that it swaps case of all letters, replaces all vowels in
// the message with the letter that appears 2 places ahead of that
// vowels in the english alphabet.
// Assume only letters.
// 
// Examples:
// >>> Encode('test')
// 'TGST'
// >>> Encode('This is a message')
// 'tHKS KS C MGSSCGG'
func Encode(message string) string {

    // Create a new string to hold the encoded message
    encodedMessage := ""

    // Iterate through each letter in the original message
    for _, letter := range message {

        // Check if the letter is a vowel
        if strings.Contains("A", "E", "I", "O", "U", "Y", letter) {

            // Check if the letter is the last letter in the alphabet
            if letter == 'Z' {
                encodedMessage += string(letter - 2)
            } else {
                encodedMessage += string(letter + 2)
            }
        } else {
            encodedMessage += string(letter)
        }
    }

    // Return the encoded message
    return encodedMessage
}

// Write a function that takes a message, and Decodes in such a
// way that it swaps case of all letters, replaces all vowels in
// the message with the letter that appears 2 places behind that
// vowels in the english alphabet.
// Assume only letters.
// 
// Examples:
// >>> Decode('test')
// 'TGST'
// >>> Decode('This is a message')
// 'tHKS KS C MGSSCGG'
func Decode(message string) string {

    // Create a new string to hold the decoded message
    decodedMessage := ""

    // Iterate through each letter in the original message
    for _, letter := range message {

        // Check if the letter is a vowel
        if strings.Contains("A", "E", "I", "O", "U", "Y",
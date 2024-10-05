import (
    "strings"
)

// Create a function Encrypt that takes a string as an argument and
// returns a string Encrypted with the alphabet being rotated.
// The alphabet should be rotated in a manner such that the letters
// shift down by two multiplied to two places.
// For example:
// Encrypt('hi') returns 'lm'
// Encrypt('asdfghjkl') returns 'ewhjklnop'
// Encrypt('gf') returns 'kj'
// Encrypt('et') returns 'ix'
func Encrypt(s string) string {
    // Create a new string that is the same length as the input string
    // and initialize it to be the empty string
    encrypted := make([]rune, len(s))
    for i := 0; i < len(s); i++ {
        // Get the index of the current character in the alphabet
        currentIndex := strings.Index(alphabet, string(s[i]))
        // Rotate the index by two multiplied by 2
        rotatedIndex := (currentIndex + 2) * 2
        // Get the character at the rotated index
        rotatedChar := alphabet[rotatedIndex]
        // Append the rotated character to the encrypted string
        encrypted = append(encrypted, rotatedChar)
    }
    return string(encrypted)
}

// The alphabet to use for encryption and decryption
const alphabet = "abcdefghijklmnopqrstuvwxyz"

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
    // Add 2 to the index of every character in order to use
    // a rotated alphabet.
    encrypted := strings.Repeat("", len(s))
    for i, c := range s {
        if c >= 'a' && c <= 'z' {
            encrypted[i] = (c + 2) % strLen
        } else {
            encrypted[i] = c
        }
    }

    return encrypted
}

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
    var out string
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            out += string(c - 2*2)
        } else if c >= 'A' && c <= 'Z' {
            out += string(c - 2*2)
        } else {
            out += string(c)
        }
    }
    return out
}

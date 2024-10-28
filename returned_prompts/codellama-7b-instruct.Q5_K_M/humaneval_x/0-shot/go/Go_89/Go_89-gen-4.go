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
    var result string
    var newStr string
    for i := 0; i < len(s); i++ {
        if (s[i] >= 'a' && s[i] <= 'm') || (s[i] >= 'A' && s[i] <= 'M') {
            newStr = s[i] + 2
            result += string(newStr)
        } else if (s[i] >= 'n' && s[i] <= 'z') || (s[i] >= 'N' && s[i] <= 'Z') {
            newStr = s[i] - 2
            result += string(newStr)
        }
    }
    return result
}



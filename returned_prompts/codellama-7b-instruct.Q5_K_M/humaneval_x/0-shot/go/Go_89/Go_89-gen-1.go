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

    // Convert the string into a []rune
    // This allows us to manipulate individual characters
    // in the string
    str := []rune(s)

    // Rotate the string by two places
    // We can do this by simply adding 2 to each character
    // in the string. We use the modulus operator to wrap
    // the character around to the beginning of the alphabet
    // if it exceeds 26
    for i := range str {
        str[i] = rune(int(str[i]) + 2) % 26
    }

    // Return the encrypted string
    return string(str)
}

// Create a function Decrypt that takes a string as an argument and
// returns a string Decrypted with the alphabet being rotated.
// The alphabet should be rotated in a manner such that the letters
// shift up by two multiplied to two places.
// For example:
// Decrypt('lm') returns 'hi'
// Decrypt('ewhjklnop') returns 'asdfghjkl'
// Decrypt('kj') returns 'gf'
// Decrypt('ix') returns 'et'
func Decrypt(s string) string {

    // Convert the string into a []rune
    // This allows us to manipulate individual characters
    // in the string
    str := []rune(s)

    // Rotate the string by two places
    // We can do this by simply subtracting 2 to each character
    // in the string. We use the modulus operator to wrap
    // the character around to the end of the alphabet
    // if it falls
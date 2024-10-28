    var result string
    for _, c := range s {
        switch {
        case c >= 'a' && c <= 'z':
            result += string((c-'a'+2*2)%26 + 'a')
        case c >= 'A' && c <= 'Z':
            result += string((c-'A'+2*2)%26 + 'A')
        default:
            result += string(c)
        }
    }
    return result
}

// Create a function Decrypt that takes an encrypted string as an argument and
// returns the decrypted string.
// Decrypt('hi') returns 'hi'
// Decrypt('ewhjklnop') returns 'asdfghjkl'
// Decrypt('kj') returns 'gf'
// Decrypt('ix') returns 'et'
func Decrypt(s string) string {

B:
    var result string
    for _, c := range s {
        switch {
        case c >= 'a' && c <= 'z':
            result += string((c-'a'-2*2+26)%26 + 'a')
        case c >= 'A' && c <= 'Z':
            result += string((c-'A'-2*2+26)%26 + 'A')
        default:
            result += string(c)
        }
    }
    return result
}

// Create a function IsRot13 that takes a string as an argument and
// returns true if the string is a Rot13 encrypted string.
// A Rot13 encryption is a simple letter substitution cipher that
// replaces a letter with the 13th letter after it in the alphabet.
// ROT13 is a special case of the Caesar cipher.
// For example:
// IsRot13('hi') returns true
// IsRot13('asdfghjkl') returns false
// IsRot13('gf') returns true
// IsRot13('et') returns false
func IsRot13(s string) bool {

C:
    for _, c := range s {
        switch {
        case c >= 'a' && c <= 'z
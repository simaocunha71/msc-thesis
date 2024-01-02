import (
    "strings"
)

// Given a string s, count the number of uppercase vowels in even indices.
// 
// For example:
// CountUpper('aBCdEf') returns 1
// CountUpper('abcdefg') returns 0
// CountUpper('dBBE') returns 0
func CountUpper(s string) int {
    var counter = 0
    for i := 0; i < strings.Len(s); i += 2 {
        if s[i:i+2] == "ae" || s[i:i+2] == "Ae" || s[i:i+2] == "Ea" || s[i:i+2] == "Ee" {
            counter += 1
        }
    }
    return counter
}

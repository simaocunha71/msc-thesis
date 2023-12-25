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
    var i = 0
    var count = 0

    for ;i < len(s); {
        if strings.ToUpper(string(s[i])) == s[i], {
            count++
            i += 1
        } else {
            break
        }
    }
    return count
}

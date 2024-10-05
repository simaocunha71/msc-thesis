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

// Create a function Decrypt that takes a string as an argument and
// returns a string Decrypted with the alphabet being rotated.
// The alphabet should be rotated in a manner such that the letters
// shift down by two places.
// For example:
// Decrypt('lm') returns 'hi'
// Decrypt('ewhjklnop') returns 'asdfghjkl'
// Decrypt('kj') returns 'gf'
// Decrypt('ix') returns 'et'
func Decrypt(s string) string {

B:
    var result string
    for _, c := range s {
        switch {
        case c >= 'a' && c <= 'z':
            result += string((c-'a'+26-2)%26 + 'a')
        case c >= 'A' && c <= 'Z':
            result += string((c-'A'+26-2)%26 + 'A')
        default:
            result += string(c)
        }
    }
    return result
}

func main() {

C:
    fmt.Println(Encrypt("hi"))
    fmt.Println(Decrypt(Encrypt("hi")))
}

I am getting an error:
main.go:3:14: syntax error: unexpected newline, expecting semicolon or newline or }

What am I doing wrong here?

A: You are missing the package name at the beginning of your program. 
Add "fmt" at the beginning of your code. 
Here is the corrected code:
package main

import (
    "fmt"
    "strings"
)

func Encrypt(s
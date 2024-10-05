    encrypted := ""

    for _, c := range s {
        if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
            if c >= 'a' && c <= 'z' {
                encrypted += string((c-'a'+2*2)%26 + 'a')
            } else if c >= 'A' && c <= 'Z' {
                encrypted += string((c-'A'+2*2)%26 + 'A')
            }
        } else {
            encrypted += string(c)
        }
    }

    return encrypted
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
    decrypted := ""

    for _, c := range s {
        if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
            if c >= 'a' && c <= 'z' {
                decrypted += string((c-'a'-2)%26 + 'a')
            } else if c >= 'A' && c <= 'Z' {
                decrypted += string((c-'A'-2)%26 + 'A')
            }
        } else {
            decrypted += string(c)
        }
    }

    return decrypted
}

*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(Encrypt("hi"))
	fmt.Println(Encrypt("asdfghjkl"))
	fmt.Println(Encrypt("gf"))
	fmt.Println(Encrypt("et"))


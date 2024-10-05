    var encrypted string
    for _, c := range s {
        switch {
        case c >= 'a' && c <= 'z':
            encrypted += string((c-'a'+2*2)%26 + 'a')
        case c >= 'A' && c <= 'Z':
            encrypted += string((c-'A'+2*2)%26 + 'A')
        default:
            encrypted += string(c)
        }
    }
    return encrypted
}

func main() {
    fmt.Println(Encrypt("hi"))
    fmt.Println(Encrypt("asdfghjkl"))
    fmt.Println(Encrypt("gf"))
    fmt.Println(Encrypt("et"))
}

Output:
lm
ewhjklnop
kj
ix
*/

package main

import (
	"fmt"
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
	var encrypted string
	for _, c := range s {
		switch {
		case c >= 'a' && c <= 'z':
			encrypted += string((c-'a'+2*2)%26 + 'a')
		case c >= 'A' && c <= 'Z':
			encrypted += string((c-'A'+2*2)%26 + 'A')
		default:
			encrypted += string(c)
		}
	}
	return encrypted
}

func main() {
	fmt.Println(Encrypt("hi"))        // returns 'lm'
	fmt.Println(Encrypt("asdfghjkl")) // returns 'ewhjklnop
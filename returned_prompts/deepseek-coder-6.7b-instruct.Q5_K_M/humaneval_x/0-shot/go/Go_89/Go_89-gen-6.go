     alphabet := "abcdefghijklmnopqrstuvwxyz"
     rotation := 2 * 2
     encrypted := ""

B:
     for _, c := range s {
         index := strings.Index(alphabet, strings.ToLower(string(c)))
         if index != -1 {
             newIndex := (index + rotation) % len(alphabet)
             encrypted += string(alphabet[newIndex])
         } else {
             encrypted += string(c)
         }
     }
     return encrypted
}

*/

package main

import (
	"fmt"
	"strings"
)

// Encrypt function
func Encrypt(s string) string {
	alphabet := "abcdefghijklmnopqrstuvwxyz"
	rotation := 2 * 2
	encrypted := ""

	for _, c := range s {
		index := strings.Index(alphabet, strings.ToLower(string(c)))
		if index != -1 {
			newIndex := (index + rotation) % len(alphabet)
			encrypted += string(alphabet[newIndex])
		} else {
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

// Output:
// lm
// ewhjklnop
// kj
// ix

/*

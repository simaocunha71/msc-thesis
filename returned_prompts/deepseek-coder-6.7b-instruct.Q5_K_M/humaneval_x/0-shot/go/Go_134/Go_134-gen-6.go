     if len(txt)==0{
         return false
     }
     lastChar := txt[len(txt)-1]
     if strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) {
         if len(txt)==1 || txt[len(txt)-2]==' ' {
             return true
         }
     }
     return false
}

The function CheckIfLastCharIsALetter checks if the last character of the string is an alphabetical character and is not a part of a word. It does this by using the 'strings' package's ContainsRune function to check if the last character is an alphabetical character. If it is, it then checks if the last character is a part of a word by checking the character before it. If it is not a part of a word, it returns true, otherwise it returns false. If the string is empty, it returns false.
*/

package main

import (
	"fmt"
	"strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
	if len(txt) == 0 {
		return false
	}
	lastChar := txt[len(txt)-1]
	if strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) {
		if len(txt) == 1 || txt[len(txt)-2] == ' ' {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(CheckIfLastCharIsALetter("apple pie"))      // ➞ false
	fmt.Println(CheckIfLastCharIsALetter("apple pi e"))     // ➞ true
	fmt.Println(CheckIfLastCharIsALetter("apple pi e "))    // ➞ false
	fmt.Println(CheckIfLastCharIsALetter(""))               // ➞ false
	fmt.Println(CheckIfLastCharIsALetter("p"))              // ➞
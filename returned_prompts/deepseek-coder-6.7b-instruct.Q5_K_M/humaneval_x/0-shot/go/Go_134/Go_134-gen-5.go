    if len(txt) <= 0 {
        return false
    }

B:
    lastChar := txt[len(txt)-1:]

C:
    if !strings.ContainsAny(lastChar, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return false
    }

D:
    if len(txt) > 1 {
        prevChar := txt[len(txt)-2:]
        if strings.ContainsAny(prevChar, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
            return false
        }
    }

E:
    return true
}

*/

package main

import (
	"fmt"
	"strings"
)

func CheckIfLastCharIsALetter(txt string) bool {

	if len(txt) <= 0 {
		return false
	}

	lastChar := txt[len(txt)-1:]

	if !strings.ContainsAny(lastChar, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
		return false
	}

	if len(txt) > 1 {
		prevChar := txt[len(txt)-2:]
		if strings.ContainsAny(prevChar, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(CheckIfLastCharIsALetter("apple pie"))      // ➞ false
	fmt.Println(CheckIfLastCharIsALetter("apple pi e"))     // ➞ true
	fmt.Println(CheckIfLastCharIsALetter("apple pi e  "))   // ➞ false
	fmt.Println(CheckIfLastCharIsALetter(""))               // ➞ false
	fmt.Println(CheckIf
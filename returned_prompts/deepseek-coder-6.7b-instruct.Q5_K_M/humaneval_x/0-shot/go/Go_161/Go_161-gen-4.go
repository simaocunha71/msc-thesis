
    // The variable to store the result
    var res string

    // Convert the string to rune array for manipulating each character
    runes := []rune(s)

    // Iterate over each rune in the string
    for _, r := range runes {

        // Check if the rune is a letter
        if unicode.IsLetter(r) {

            // If it's upper case, convert it to lower case
            if unicode.IsUpper(r) {
                res += string(unicode.ToLower(r))
            } else { // It's lower case, convert it to upper case
                res += string(unicode.ToUpper(r))
            }
        } else { // If it's not a letter, keep it as it is
            res += string(r)
        }
    }

    // If no letter was found in the string, reverse it
    if len(res) == len(s) {
        return reverse(res)
    }

    return res
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

*/

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func Solve(s string) string {

	var res string

	runes := []rune(s)

	for _, r := range runes {
		if unicode.IsLetter(r) {
			if unicode.IsUpper(r) {
				res += string(unicode.ToLower(r))
			} else {
				res += string(unicode.ToUpper(r))
			}
		} else {
			res += string(r)
		}
	}

	if len(res) == len(s) {
		return reverse(res)
	}

    var flipped string

B:
    for _, char := range str {
        if unicode.IsLower(char) {
            flipped += strings.ToUpper(string(char))
        } else if unicode.IsUpper(char) {
            flipped += strings.ToLower(string(char))
        } else {
            flipped += string(char)
        }
    }

C:
    return flipped
}

*/

import (
	"strings"
	"unicode"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
func FlipCase(str string) string {
	var flipped string

	for _, char := range str {
		if unicode.IsLower(char) {
			flipped += strings.ToUpper(string(char))
		} else if unicode.IsUpper(char) {
			flipped += strings.ToLower(string(char))
		} else {
			flipped += string(char)
		}
	}

	return flipped
}

func main() {
	fmt.Println(FlipCase("Hello")) // Output: 'hELLO'
}

/*
Output:
hELLO
*/

/*
Question:
Given a string, return a new string where "not " has been added to the front of a given string if the given string does not begin with "not ". If the string already begins with "not ", return the string unchanged.

Function Signature:

func AddNot(str string) string {

}

Example:

AddNot("Hello") -> "not Hello"
AddNot("not Hello") -> "not Hello"

*/

package main

import (
	"fmt"
	"strings"
)

func AddNot(str string) string {
	if strings.HasPrefix(str, "not ") {
		return str
	} else {
		return "not " + str
	}
}

func main() {
	fmt.Println(AddNot("Hello"))       // Output: 'not Hello'
	fmt.Println(AddNot("not H
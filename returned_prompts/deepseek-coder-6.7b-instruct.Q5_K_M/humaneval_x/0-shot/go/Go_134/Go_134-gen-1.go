    
B:

C:

D:

E:

F:

}
*/

import (
	"strings"
	"unicode"
)

func CheckIfLastCharIsALetter(txt string) bool {
	if len(txt) == 0 {
		return false
	}
	lastRune := txt[len(txt)-1]
	if unicode.IsLetter(rune(lastRune)) && !strings.ContainsRune(" ", rune(lastRune)) {
		return true
	}
	return false
}

func main() {
	fmt.Println(CheckIfLastCharIsALetter("apple pie"))  // ➞ false
	fmt.Println(CheckIfLastCharIsALetter("apple pi e")) // ➞ true
	fmt.Println(CheckIfLastCharIsALetter("apple pi e ")) // ➞ false
	fmt.Println(CheckIfLastCharIsALetter("")) // ➞ false
}

import (
	"strings"
)

func CorrectBracketing(brackets string) bool {
	open := 0
	for _, b := range brackets {
		if b == '(' {
			open++
		} else if b == ')' {
			open--
		}
		if open < 0 {
			return false
		}
	}
	return open == 0
}

func main() {
	println(CorrectBracketing("("))    // false
	println(CorrectBracketing("()"))   // true
	println(CorrectBracketing("(()())"))   // true
	println(CorrectBracketing(")(()")) // false
}